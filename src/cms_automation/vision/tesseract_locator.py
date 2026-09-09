"""Localização automática do executável do Tesseract OCR.

Objetivo: a pessoa que só descarrega o executável standalone não deve
precisar de descobrir/escrever o caminho do Tesseract à mão. Se
appsettings.yaml tiver `tesseract_cmd: auto`, tentamos, por ordem:

  1. Uma cópia do Tesseract embutida ao lado do executável (pasta
     `tesseract/` — é isto que o bundle do Windows traz incluído).
  2. O Tesseract já instalado no sistema (PATH).
  3. Localizações típicas de instalação no Windows/Linux/macOS.

Se nada for encontrado, falha com uma mensagem clara em vez de um erro
críptico do pytesseract lá dentro.
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

AUTO = "auto"

_COMMON_PATHS = [
    "/usr/bin/tesseract",
    "/usr/local/bin/tesseract",
    "/opt/homebrew/bin/tesseract",
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
]


class TesseractNotFoundError(Exception):
    pass


def _executable_dir() -> Path:
    """Pasta onde o executável (ou o script) está a correr.

    Quando empacotado com PyInstaller (--onefile), `sys.executable` é o
    próprio binário; em modo normal (`python -m cms_automation.cli`),
    usamos a pasta de trabalho atual como aproximação razoável.
    """
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    return Path.cwd()


def resolve_tesseract_cmd(configured_value: str) -> str:
    """Devolve o caminho do executável do Tesseract a usar.

    Se `configured_value` não for "auto", é devolvido tal e qual
    (comportamento explícito, tal como antes).
    """
    if configured_value.strip().lower() != AUTO:
        return configured_value

    # 1. Cópia embutida ao lado do executável
    bundled_names = ["tesseract/tesseract.exe", "tesseract/tesseract"]
    for name in bundled_names:
        candidate = _executable_dir() / name
        if candidate.exists():
            return str(candidate)

    # 2. PATH do sistema
    found = shutil.which("tesseract")
    if found:
        return found

    # 3. Localizações típicas
    for path_str in _COMMON_PATHS:
        if Path(path_str).exists():
            return path_str

    raise TesseractNotFoundError(
        "Não foi possível encontrar o Tesseract OCR automaticamente.\n"
        "Instale-o (sudo apt install tesseract-ocr no Linux; "
        "https://github.com/UB-Mannheim/tesseract/wiki no Windows; "
        "brew install tesseract no macOS), ou defina o caminho exato "
        "em appsettings.yaml -> ocr.tesseract_cmd."
    )
