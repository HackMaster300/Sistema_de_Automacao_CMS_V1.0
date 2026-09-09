"""Ponto de entrada da linha de comandos.

Exemplos:
    python -m cms_automation.cli --appsettings config/appsettings.yaml
    python -m cms_automation.cli --appsettings config/appsettings.yaml --dry-run
    python -m cms_automation.cli --appsettings config/appsettings.yaml --data data/lote_2026_01.xlsx
"""
from __future__ import annotations

import argparse
import logging
import sys

from .config import ConfigError, load_config
from .data_source import open_data_source
from .input.fake_controller import FakeInputController
from .input.real_controller import RealInputController
from .logging_setup import setup_logging
from .vision.fake_backend import FakeVisionBackend
from .vision.ocr_backend import TesseractVisionBackend
from .workflow.processor import process_batch

logger = logging.getLogger(__name__)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Automação CMS")
    parser.add_argument(
        "--appsettings",
        "--config",
        dest="appsettings",
        required=True,
        help="Caminho para o ficheiro appsettings.yaml (coordenadas, OCR, tempos)",
    )
    parser.add_argument(
        "--data",
        default=None,
        help="CSV ou Excel com os identificadores a processar e checkpoint "
        "(sobrepõe data_file do appsettings)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Não mexe no rato/teclado real nem lê o ecrã; simula a execução",
    )
    parser.add_argument(
        "--verbose", action="store_true", help="Logging em modo DEBUG"
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)

    try:
        config = load_config(args.appsettings)
    except ConfigError as exc:
        print(f"Erro de configuração: {exc}", file=sys.stderr)
        return 1

    setup_logging(config.log_dir, level=logging.DEBUG if args.verbose else logging.INFO)

    data_path = args.data or config.data_file
    try:
        data_source = open_data_source(data_path)
    except (FileNotFoundError, ValueError) as exc:
        logger.error(str(exc))
        return 1

    dry_run = args.dry_run or config.dry_run
    if dry_run:
        logger.info("Modo --dry-run: nenhuma ação real será executada.")
        input_ctrl = FakeInputController()
        vision = FakeVisionBackend()
    else:
        input_ctrl = RealInputController()
        vision = TesseractVisionBackend(config.tesseract_cmd)

    resumo_inicial = data_source.summary()
    logger.info(
        "Ficheiro de dados: %d pendente(s), %d concluído(s), %d com erro.",
        resumo_inicial.get("pendente", 0),
        resumo_inicial.get("concluido", 0),
        resumo_inicial.get("erro", 0),
    )

    stats = process_batch(data_source, config, input_ctrl, vision)
    print(stats.summary_text())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
