"""Motor de execução de passos de UI, orientado a dados.

O V1.0 repetia a mesma sequência de ~120 cliques/teclas quatro vezes ao
longo do ficheiro (uma por cada estado x variação de OCR), copiada e
colada com pequenas divergências acidentais entre cópias. Aqui a
sequência existe uma única vez, como dados (lista de Step), e é
executada por este motor — reutilizável, testável e sem duplicação.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum, auto

from ..config import AppConfig
from ..input.base import InputController
from ..vision.base import VisionBackend

logger = logging.getLogger(__name__)


class StepKind(Enum):
    CLICK = auto()          # clica numa coordenada nomeada
    TYPE_THEN_TAB = auto()  # escreve um valor (tecla a tecla) e avança com Tab
    KEY = auto()            # uma única tecla/atalho (ex: 'enter', 'shift+tab')
    SLEEP = auto()
    OCR_CHECK = auto()      # lê uma região e, se o texto bater certo, envia uma tecla extra
    PASTE_TEXT = auto()     # copia o valor para a área de transferência e cola (Ctrl+V)


@dataclass(frozen=True)
class Step:
    kind: StepKind
    coordinate: str | None = None
    clicks: int = 1
    value: str | None = None
    seconds: float | None = None
    region: str | None = None
    expected_text: str | None = None
    extra_key_if_match: str | None = None


class StepRunner:
    """Executa uma lista de Step usando um InputController e VisionBackend
    concretos (reais ou falsos, para testes/dry-run)."""

    def __init__(
        self,
        config: AppConfig,
        input_ctrl: InputController,
        vision: VisionBackend,
    ) -> None:
        self._config = config
        self._input = input_ctrl
        self._vision = vision

    def run(self, steps: list[Step]) -> None:
        for step in steps:
            self._run_one(step)

    def _run_one(self, step: Step) -> None:
        timing = self._config.timing

        if step.kind is StepKind.CLICK:
            point = self._config.coordinates.get(step.coordinate)
            self._input.click(point, clicks=step.clicks)
            self._input.sleep(timing.click_pause)

        elif step.kind is StepKind.TYPE_THEN_TAB:
            for char in step.value or "":
                self._input.press_key(char)
                self._input.sleep(timing.short_pause)
            self._input.press_key("tab")
            self._input.sleep(timing.short_pause)

        elif step.kind is StepKind.KEY:
            self._input.press_key(step.value or "")
            self._input.sleep(timing.short_pause)

        elif step.kind is StepKind.SLEEP:
            self._input.sleep(step.seconds or timing.short_pause)

        elif step.kind is StepKind.PASTE_TEXT:
            self._input.type_text(step.value or "")
            self._input.sleep(timing.click_pause)

        elif step.kind is StepKind.OCR_CHECK:
            region = getattr(self._config.ocr, step.region)
            texto = self._vision.read_text(region).strip().replace("\n", "")
            logger.debug("OCR_CHECK leu %r (esperado %r)", texto, step.expected_text)
            if texto == step.expected_text and step.extra_key_if_match:
                self._input.press_key(step.extra_key_if_match)
                self._input.sleep(timing.short_pause)

        else:  # pragma: no cover - defensivo
            raise ValueError(f"StepKind desconhecido: {step.kind}")
