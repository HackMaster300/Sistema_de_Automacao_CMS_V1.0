#!/usr/bin/env python3
"""Monta a pasta final "pronta a usar" que vai para a Release.

Junta num só sítio: o executável principal, o executável de
calibração, um appsettings.yaml já preenchido (valores de exemplo,
prontos para calibrar), os dados de exemplo, as pastas vazias
necessárias (assets/error_templates, logs), o guia rápido, e — se
existir — uma cópia do Tesseract embutida (ver --tesseract-dir).

Uso:
    python packaging/assemble_bundle.py \\
        --os linux \\
        --exe-path dist/cms-automation-linux \\
        --calibrate-exe-path dist/calibrate-coordinates-linux \\
        --output-dir bundle
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def assemble(
    os_name: str,
    exe_path: Path,
    calibrate_exe_path: Path,
    output_dir: Path,
    tesseract_dir: Path | None,
) -> None:
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    # Executáveis
    shutil.copy2(exe_path, output_dir / exe_path.name)
    shutil.copy2(calibrate_exe_path, output_dir / calibrate_exe_path.name)
    if os_name != "windows":
        (output_dir / exe_path.name).chmod(0o755)
        (output_dir / calibrate_exe_path.name).chmod(0o755)

    # appsettings.yaml já pronto (copiado do exemplo — nunca gerado do nada)
    shutil.copy2(
        ROOT / "config" / "appsettings.example.yaml", output_dir / "appsettings.yaml"
    )

    # Dados de exemplo, prontos para o utilizador substituir
    dados_dir = output_dir / "dados"
    dados_dir.mkdir()
    shutil.copy2(
        ROOT / "data" / "sample_identifiers.csv",
        dados_dir / "identificadores.csv",
    )

    # Pastas necessárias, vazias
    (output_dir / "assets" / "error_templates").mkdir(parents=True)
    (output_dir / "logs").mkdir()

    # Guia rápido e documentação
    shutil.copy2(ROOT / "packaging" / "COMO_COMECAR.txt", output_dir / "COMO_COMECAR.txt")
    shutil.copy2(ROOT / "LICENSE", output_dir / "LICENSE")
    shutil.copy2(ROOT / "CHANGELOG.md", output_dir / "CHANGELOG.md")

    # Tesseract embutido, se o passo anterior do CI o tiver preparado
    if tesseract_dir and tesseract_dir.exists():
        shutil.copytree(tesseract_dir, output_dir / "tesseract")
        print(f"Tesseract embutido incluído a partir de {tesseract_dir}")
    else:
        print(
            "Aviso: nenhum Tesseract embutido fornecido — o utilizador "
            "final terá de o instalar à parte (ver COMO_COMECAR.txt)."
        )

    print(f"Bundle montado em: {output_dir}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--os", required=True, choices=["linux", "windows", "macos"])
    parser.add_argument("--exe-path", required=True, type=Path)
    parser.add_argument("--calibrate-exe-path", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument(
        "--tesseract-dir",
        type=Path,
        default=None,
        help="Pasta com um Tesseract já preparado para embutir (opcional)",
    )
    args = parser.parse_args()

    assemble(
        args.os, args.exe_path, args.calibrate_exe_path, args.output_dir, args.tesseract_dir
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
