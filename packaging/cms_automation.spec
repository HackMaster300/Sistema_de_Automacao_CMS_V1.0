# -*- mode: python ; coding: utf-8 -*-
"""Spec do PyInstaller — gera um executável único (--onefile) para
Windows, Linux ou macOS, consoante o SO onde for corrido.

Uso:
    pyinstaller packaging/cms_automation.spec

O binário fica em dist/cms-automation (ou dist/cms-automation.exe no
Windows). O workflow .github/workflows/release.yml corre isto
automaticamente em cada SO e anexa o resultado à GitHub Release.
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
    ["entrypoint.py"],
    pathex=["../src"],
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
    name="cms-automation",
    debug=False,
    strip=False,
    upx=False,
    console=True,
    onefile=True,
)
