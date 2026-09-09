"""Interface abstrata para controlo de rato e teclado.

Tal como a visão computacional, isto permite testar toda a lógica de
"o que fazer para cada estado" sem mexer no rato/teclado reais, e abre
a porta a trocar PyAutoGUI por outra biblioteca de RPA no futuro.
"""
from __future__ import annotations

from abc import ABC, abstractmethod

from ..config import Point


class InputController(ABC):
    @abstractmethod
    def click(self, point: Point, clicks: int = 1) -> None: ...

    @abstractmethod
    def move_to(self, x: int, y: int) -> None: ...

    @abstractmethod
    def type_text(self, text: str) -> None: ...

    @abstractmethod
    def press_key(self, key: str) -> None: ...

    @abstractmethod
    def sleep(self, seconds: float) -> None: ...
