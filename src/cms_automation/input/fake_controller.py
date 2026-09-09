"""InputController falso: regista cada ação num log em memória em vez de
mexer no rato/teclado real. Usado em testes e no modo --dry-run — permite
validar toda a sequência de passos que seria executada, em segurança."""
from __future__ import annotations

from ..config import Point
from .base import InputController


class FakeInputController(InputController):
    def __init__(self) -> None:
        self.actions: list[tuple[str, object]] = []

    def click(self, point: Point, clicks: int = 1) -> None:
        self.actions.append(("click", (point, clicks)))

    def move_to(self, x: int, y: int) -> None:
        self.actions.append(("move_to", (x, y)))

    def type_text(self, text: str) -> None:
        self.actions.append(("type_text", text))

    def press_key(self, key: str) -> None:
        self.actions.append(("press_key", key))

    def sleep(self, seconds: float) -> None:
        self.actions.append(("sleep", seconds))
