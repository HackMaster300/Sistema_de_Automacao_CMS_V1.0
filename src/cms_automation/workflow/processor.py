"""Orquestração do processamento em lote.

Equivalente ao loop principal do V1.0 (inserir -> verificar erro -> OCR
-> decidir ação), mas decomposto em funções pequenas e testáveis, com
logging em vez de `print`, e com um travão explícito para casos
sinalizados como suspeita de fraude (ver `require_confirmation_for_fraud_flag`
em config.yaml).
"""
from __future__ import annotations

import logging
from enum import Enum, auto

from ..config import AppConfig
from ..data_source import CheckpointDataSource, RecordStatus
from ..input.base import InputController
from ..parsing import parse_ocr_text
from ..stats import ProcessingStats
from ..vision.base import VisionBackend
from ..workflow.actions import build_navigate_to_registration_steps, build_registration_steps
from ..workflow.states import ParsedRecord, RecordState
from ..workflow.steps import Step, StepKind, StepRunner

logger = logging.getLogger(__name__)


class ErrorCheckResult(Enum):
    NONE = auto()
    RECOVERABLE = auto()
    CRITICAL = auto()


class CriticalUIError(Exception):
    """Estado inesperado da interface que exige paragem e verificação manual."""


def insert_identifier(runner: StepRunner, config: AppConfig, identifier: str) -> None:
    steps = [
        Step(StepKind.CLICK, coordinate="campo_pf", clicks=2),
        Step(StepKind.SLEEP, seconds=0.9),
        Step(StepKind.CLICK, coordinate="botao_contador"),
        Step(StepKind.SLEEP, seconds=0.1),
    ]
    runner.run(steps)
    runner.run(
        [
            Step(StepKind.PASTE_TEXT, value=identifier),
            Step(StepKind.KEY, value="enter"),
            Step(StepKind.SLEEP, seconds=0.5),
            Step(StepKind.KEY, value="enter"),
            Step(StepKind.SLEEP, seconds=0.5),
        ]
    )


def check_for_error(vision: VisionBackend, config: AppConfig, runner: StepRunner) -> ErrorCheckResult:
    templates = config.error_templates

    if vision.locate_on_screen(templates.primary, templates.confidence_primary):
        runner.run([Step(StepKind.CLICK, coordinate="botao_ok_erro")])
        return ErrorCheckResult.RECOVERABLE

    if vision.locate_on_screen(templates.secondary, templates.confidence_secondary):
        runner.run([Step(StepKind.CLICK, coordinate="botao_ok_erro")])
        return ErrorCheckResult.RECOVERABLE

    # Nenhum erro primário/secundário: tenta avançar clicando na área principal
    runner.run(
        [
            Step(StepKind.CLICK, coordinate="area_clique_confirmacao", clicks=2),
            Step(StepKind.SLEEP, seconds=1.0),
        ]
    )

    if vision.locate_on_screen(templates.tertiary, templates.confidence_tertiary):
        runner.run(
            [
                Step(StepKind.CLICK, coordinate="botao_ok_erro"),
                Step(StepKind.SLEEP, seconds=2.0),
                Step(StepKind.KEY, value="enter"),
                Step(StepKind.SLEEP, seconds=2.0),
            ]
        )
        return ErrorCheckResult.CRITICAL

    return ErrorCheckResult.NONE


def read_and_parse(vision: VisionBackend, config: AppConfig) -> list[ParsedRecord]:
    texto = vision.read_text(config.ocr.ocr_region)
    logger.debug("Texto OCR bruto: %r", texto)
    return parse_ocr_text(texto)


def dispatch_record(
    record: ParsedRecord,
    runner: StepRunner,
    config: AppConfig,
    stats: ProcessingStats,
) -> None:
    if record.flagged_for_fraud_review and config.require_confirmation_for_fraud_flag:
        stats.contador_fraude_pendente_revisao += 1
        logger.warning(
            "OT %s marcada como 'suspeita de fraude' — deixada para revisão "
            "manual (require_confirmation_for_fraud_flag=true). Linha: %r",
            record.ot_number,
            record.raw_line,
        )
        return

    if record.state is RecordState.REGISTADO:
        stats.contador_registados += 1
        runner.run(build_navigate_to_registration_steps())
        runner.run(build_registration_steps(config.form_defaults))

    elif record.state is RecordState.EM_PROCESSAMENTO:
        stats.contador_em_processamento += 1
        runner.run(build_navigate_to_registration_steps())
        runner.run(build_registration_steps(config.form_defaults))

    else:  # INTRODUZIDO / nenhuma keyword reconhecida
        stats.contador_introduzido += 1
        logger.info("OT %s: fluxo padrão (introduzido), nenhuma ação adicional.", record.ot_number)


def process_batch(
    data_source: CheckpointDataSource,
    config: AppConfig,
    input_ctrl: InputController,
    vision: VisionBackend,
    stats: ProcessingStats | None = None,
    cancel_event=None,
) -> ProcessingStats:
    """Processa apenas os registos ainda "pendente" na fonte de dados.

    Cada identificador é marcado como "concluido" ou "erro" no próprio
    ficheiro (CSV/Excel) logo a seguir a ser processado — isto é o
    checkpoint: se o processo for interrompido, a próxima execução
    retoma automaticamente a partir dos registos que ainda faltam,
    sem reprocessar os já feitos.

    `cancel_event` é opcional (um `threading.Event`, tipicamente vindo
    da GUI): se for passado e for sinalizado, o lote pára de forma
    limpa a seguir ao identificador em curso — nunca a meio de um, para
    não deixar o checkpoint inconsistente.
    """
    stats = stats or ProcessingStats()
    runner = StepRunner(config, input_ctrl, vision)

    pendentes = data_source.pending()
    logger.info(
        "%d registo(s) pendente(s) de um total de %d no ficheiro de dados.",
        len(pendentes),
        len(data_source.load_all()),
    )

    for record_data in pendentes:
        if cancel_event is not None and cancel_event.is_set():
            logger.info("Cancelamento solicitado — a parar antes do próximo identificador.")
            break

        identifier = record_data.identificador
        logger.info("Processando identificador: %s", identifier)

        try:
            insert_identifier(runner, config, identifier)
            stats.total_processados += 1

            error_result = check_for_error(vision, config, runner)
            if error_result is ErrorCheckResult.RECOVERABLE:
                stats.numeros_errados += 1
                logger.warning("Erro recuperável detetado para %s.", identifier)
                data_source.mark(identifier, RecordStatus.ERRO)
                continue
            if error_result is ErrorCheckResult.CRITICAL:
                stats.numeros_errados += 1
                logger.error(
                    "Erro crítico de interface para %s — a parar o lote para verificação manual.",
                    identifier,
                )
                data_source.mark(identifier, RecordStatus.ERRO)
                break

            records = read_and_parse(vision, config)
            if not records:
                logger.warning("Nenhuma linha reconhecida no OCR para %s.", identifier)
                data_source.mark(identifier, RecordStatus.ERRO)
                continue

            for record in records:
                dispatch_record(record, runner, config, stats)

            data_source.mark(identifier, RecordStatus.CONCLUIDO)

        except Exception:
            logger.exception("Falha inesperada ao processar %s. A parar o lote.", identifier)
            data_source.mark(identifier, RecordStatus.ERRO)
            break

    stats.finish()
    return stats
