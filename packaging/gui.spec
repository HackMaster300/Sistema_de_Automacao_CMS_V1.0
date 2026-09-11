# -*- mode: python ; coding: utf-8 -*-
"""Spec do PyInstaller para a GUI (Tkinter) — janela, sem consola.

Uso:
    pyinstaller packaging/gui.spec
"""
from PyInstaller.utils.hooks import collect_submodules

hidden_imports = (
    collect_submodules("pyautogui")
    + collect_submodules("pytesseract")
    + collect_submodules("keyboard")
    + collect_submodules("openpyxl")
    + collect_submodules("PIL")
)

a = Analysis(
    ["gui_entrypoint.py"],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="cms-automation-gui",
    debug=False,
    strip=False,
    upx=False,
    console=False,  # janela, sem consola atrás
    onefile=True,
)
