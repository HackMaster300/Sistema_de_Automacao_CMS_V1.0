"""Controlo real de rato/teclado — equivalente direto ao que o V1.0 fazia
inline, mas isolado atrás de InputController."""
from __future__ import annotations

import logging
import time

from ..config import Point
from .base import InputController

logger = logging.getLogger(__name__)


class RealInputController(InputController):
    def __init__(self) -> None:
        import keyboard
        import pyautogui
        import pyperclip

        self._pyautogui = pyautogui
        self._keyboard = keyboard
        self._pyperclip = pyperclip

    def click(self, point: Point, clicks: int = 1) -> None:
        logger.debug("click em %s (clicks=%s)", point, clicks)
        self._pyautogui.click(point.x, point.y, button="left", clicks=clicks, interval=0.25)

    def move_to(self, x: int, y: int) -> None:
        self._pyautogui.moveTo(x, y)
        self._pyautogui.click()

    def type_text(self, text: str) -> None:
        self._pyperclip.copy(text)
        self._pyautogui.hotkey("ctrl", "v")

    def press_key(self, key: str) -> None:
        self._keyboard.press_and_release(key)

    def sleep(self, seconds: float) -> None:
        time.sleep(seconds)
