"""Ponto de entrada usado pelo PyInstaller para gerar o executável
gráfico standalone (cms-automation-gui.exe / cms-automation-gui)."""
from cms_automation.gui.app import main

if __name__ == "__main__":
    raise SystemExit(main())
