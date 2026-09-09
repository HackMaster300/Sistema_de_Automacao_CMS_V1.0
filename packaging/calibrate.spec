# -*- mode: python ; coding: utf-8 -*-
"""Spec do PyInstaller para tools/calibrate_coordinates.py — gera um
segundo executável (calibrate-coordinates), para que a calibração
também não precise de Python instalado.

Uso:
    pyinstaller packaging/calibrate.spec
"""
from PyInstaller.utils.hooks import collect_submodules

hidden_imports = (
    collect_submodules("pyautogui")
    + collect_submodules("ruamel.yaml")
    + collect_submodules("PIL")
)

a = Analysis(
    ["../tools/calibrate_coordinates.py"],
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
    name="calibrate-coordinates",
    debug=False,
    strip=False,
    upx=False,
    console=True,
    onefile=True,
)
