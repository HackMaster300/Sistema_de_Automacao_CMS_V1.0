"""Backend de visão computacional baseado em PyAutoGUI + Tesseract OCR.

Esta é a implementação "fiel ao original" — mesma tecnologia do V1.0 —
mas isolada atrás de VisionBackend, para que a lógica de negócio nunca
importe pyautogui/pytesseract diretamente.
"""
from __future__ import annotations

import logging
from pathlib import Path

from ..config import Region
from .base import VisionBackend
from .tesseract_locator import resolve_tesseract_cmd

logger = logging.getLogger(__name__)


class TesseractVisionBackend(VisionBackend):
    def __init__(self, tesseract_cmd: str) -> None:
        # Imports pesados/opcionais só acontecem aqui, para que o resto do
        # pacote (parsing, stats, testes) não dependa de pyautogui/tesseract
        # estarem instalados.
        import pyautogui
        import pytesseract

        resolved_cmd = resolve_tesseract_cmd(tesseract_cmd)
        logger.info("A usar Tesseract em: %s", resolved_cmd)
        pytesseract.pytesseract.tesseract_cmd = resolved_cmd
        self._pyautogui = pyautogui
        self._pytesseract = pytesseract

    def read_text(self, region: Region) -> str:
        screenshot = self._pyautogui.screenshot(region=region.as_tuple())
        texto = self._pytesseract.image_to_string(screenshot)
        logger.debug("OCR lido de %s: %r", region, texto)
        return texto

    def locate_on_screen(self, template_path: str | Path, confidence: float) -> bool:
        try:
            resultado = self._pyautogui.locateOnScreen(
                str(template_path), confidence=confidence
            )
            return resultado is not None
        except self._pyautogui.ImageNotFoundException:
            return False
