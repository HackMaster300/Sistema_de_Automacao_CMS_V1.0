"""Interface abstrata para qualquer backend de visão computacional.

O V1.0 chamava pytesseract e pyautogui.locateOnScreen diretamente,
espalhado por 2800 linhas. Isso torna impossível testar a lógica de
negócio sem um ecrã real, e impossível trocar o motor de OCR (por
exemplo, para um serviço cloud, ou para EasyOCR) sem reescrever tudo.

Qualquer novo backend só precisa de implementar esta interface.
"""
from __future__ import annotations

from abc import ABC, abstractmethod

from ..config import Region


class VisionBackend(ABC):
    @abstractmethod
    def read_text(self, region: Region) -> str:
        """Captura a região do ecrã indicada e devolve o texto reconhecido."""

    @abstractmethod
    def locate_on_screen(self, template_path, confidence: float) -> bool:
        """Devolve True se a imagem-modelo for encontrada no ecrã atual."""
