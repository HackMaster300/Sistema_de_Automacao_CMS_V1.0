"""Backend de visão falso: devolve dados pré-programados em vez de olhar
para o ecrã. Usado em testes automatizados e no modo --dry-run, onde não
existe (ou não se quer usar) um ecrã real.
"""
from __future__ import annotations

from pathlib import Path

from ..config import Region
from .base import VisionBackend


class FakeVisionBackend(VisionBackend):
    def __init__(
        self,
        scripted_texts: list[str] | None = None,
        error_found: bool = False,
    ) -> None:
        self._scripted_texts = list(scripted_texts or [])
        self._error_found = error_found
        self.read_calls: list[Region] = []
        self.locate_calls: list[tuple[str, float]] = []

    def read_text(self, region: Region) -> str:
        self.read_calls.append(region)
        if self._scripted_texts:
            return self._scripted_texts.pop(0)
        return ""

    def locate_on_screen(self, template_path: str | Path, confidence: float) -> bool:
        self.locate_calls.append((str(template_path), confidence))
        return self._error_found
