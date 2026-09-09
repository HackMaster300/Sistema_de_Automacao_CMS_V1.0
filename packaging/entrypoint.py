"""Ponto de entrada usado pelo PyInstaller para gerar o executável
standalone (cms-automation.exe no Windows, cms-automation no
Linux/macOS).

Não é usado quando o pacote é instalado via pip (aí o entry point é
`cms_automation.cli:main`, definido em pyproject.toml) — este ficheiro
existe só para dar ao PyInstaller um único ponto de partida óbvio.
"""
from cms_automation.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
