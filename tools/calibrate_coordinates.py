#!/usr/bin/env python3
"""Ferramenta de calibração de coordenadas (linha de comandos).

A mesma lógica de leitura/escrita do appsettings.yaml é partilhada com
a GUI, através de cms_automation.appsettings_editor — para não haver
dois sítios a saber gravar o ficheiro.

Uso:
    python tools/calibrate_coordinates.py mouse
    python tools/calibrate_coordinates.py region
    python tools/calibrate_coordinates.py list --appsettings config/appsettings.yaml
    python tools/calibrate_coordinates.py capture --appsettings config/appsettings.yaml
    python tools/calibrate_coordinates.py capture --appsettings config/appsettings.yaml --only botao_ok_erro,botao_anterior
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from cms_automation.appsettings_editor import (  # noqa: E402
    AppsettingsEditError,
    get_coordinate,
    list_coordinate_names,
    load_editable,
    save_editable,
    update_coordinate,
)


def watch_mouse_position() -> None:
    import pyautogui

    print("Posicione o cursor sobre o ponto desejado.")
    print("As coordenadas serão impressas a cada 2 segundos. Ctrl+C para parar.\n")
    try:
        while True:
            x, y = pyautogui.position()
            print(f"Coordenadas atuais: ({x}, {y})")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nCalibração de posição interrompida.")


def compute_region() -> None:
    print("Introduza os cantos da região a capturar (canto superior-esquerdo e inferior-direito).")
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))

    largura = x2 - x1
    altura = y2 - y1
    print(f"\nRegião calculada: x={x1}, y={y1}, width={largura}, height={altura}")
    print("Cole isto no appsettings.yaml no formato:")
    print(f"  {{ x: {x1}, y: {y1}, width: {largura}, height: {altura} }}")


def list_coordinates(appsettings_path: Path) -> None:
    try:
        _, data = load_editable(appsettings_path)
    except AppsettingsEditError as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)

    names = list_coordinate_names(data)
    if not names:
        print("Nenhuma coordenada encontrada em 'coordinates:'.")
        return

    print(f"{'nome':35s} x      y")
    print("-" * 50)
    for name in names:
        x, y = get_coordinate(data, name)
        print(f"{name:35s} {x:<6} {y}")


def capture_coordinates(appsettings_path: Path, only: list[str] | None) -> None:
    import pyautogui

    try:
        yaml, data = load_editable(appsettings_path)
    except AppsettingsEditError as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)

    all_names = list_coordinate_names(data)
    names = only or all_names
    unknown = [n for n in names if n not in all_names]
    if unknown:
        print(f"Nomes desconhecidos: {', '.join(unknown)}", file=sys.stderr)
        raise SystemExit(1)

    print(f"A calibrar {len(names)} coordenada(s). Para cada uma:")
    print("  1. Posicione o rato exatamente sobre o elemento na interface do CMS")
    print("  2. Volte a esta janela e pressione Enter\n")

    captured: dict[str, tuple[int, int]] = {}
    for name in names:
        old_x, old_y = get_coordinate(data, name)
        input(f"[{name}] (atual: {old_x}, {old_y}) — posicione o rato e pressione Enter...")
        x, y = pyautogui.position()
        captured[name] = (x, y)
        print(f"  -> capturado: ({x}, {y})\n")

    print("Resumo das novas coordenadas:")
    print(f"{'nome':35s} {'antes':15s} depois")
    print("-" * 65)
    for name, (x, y) in captured.items():
        old_x, old_y = get_coordinate(data, name)
        print(f"{name:35s} ({old_x}, {old_y})".ljust(51) + f"({x}, {y})")

    resposta = input(f"\nGravar estas coordenadas em {appsettings_path}? [s/N] ").strip().lower()
    if resposta != "s":
        print("Nada foi gravado.")
        return

    for name, (x, y) in captured.items():
        update_coordinate(data, name, x, y)

    save_editable(yaml, data, appsettings_path)
    print(f"Coordenadas gravadas em {appsettings_path}.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Calibração de coordenadas de UI")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("mouse", help="Imprime a posição do rato continuamente")
    sub.add_parser("region", help="Calcula width/height a partir de dois cantos")

    list_parser = sub.add_parser("list", help="Lista as coordenadas do appsettings")
    list_parser.add_argument("--appsettings", required=True)

    capture_parser = sub.add_parser(
        "capture", help="Captura coordenadas e grava no appsettings, após confirmação"
    )
    capture_parser.add_argument("--appsettings", required=True)
    capture_parser.add_argument(
        "--only", default=None, help="Lista de nomes separados por vírgula (por omissão, recalibra todas)"
    )

    args = parser.parse_args()

    if args.command == "mouse":
        watch_mouse_position()
    elif args.command == "region":
        compute_region()
    elif args.command == "list":
        list_coordinates(Path(args.appsettings))
    elif args.command == "capture":
        only = args.only.split(",") if args.only else None
        capture_coordinates(Path(args.appsettings), only)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
