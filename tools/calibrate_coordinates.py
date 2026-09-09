#!/usr/bin/env python3
"""Ferramenta de calibração de coordenadas.

Substitui o antigo coordenadas.py. Além de ajudar a descobrir posições
do rato e regiões de ecrã, o modo `capture` grava as coordenadas
DIRETAMENTE no appsettings.yaml (depois de você confirmar), preservando
comentários e todo o resto do ficheiro — nunca mais copiar/colar
números à mão.

Uso:
    python tools/calibrate_coordinates.py mouse
        Imprime a posição do rato a cada 2 segundos (Ctrl+C para parar).

    python tools/calibrate_coordinates.py region
        Ajuda a calcular width/height de uma região a partir de dois cantos.

    python tools/calibrate_coordinates.py list --appsettings config/appsettings.yaml
        Lista as coordenadas atualmente configuradas.

    python tools/calibrate_coordinates.py capture --appsettings config/appsettings.yaml
        Para cada coordenada já existente no ficheiro, pede para
        posicionar o rato e pressionar Enter; no fim, mostra um resumo
        e só grava no appsettings.yaml se você confirmar.

    python tools/calibrate_coordinates.py capture --appsettings config/appsettings.yaml --only botao_ok_erro,botao_anterior
        Recalibra só as coordenadas indicadas, em vez de todas.
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path


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


def _load_yaml(path: Path):
    from ruamel.yaml import YAML

    yaml = YAML()
    yaml.preserve_quotes = True
    with path.open("r", encoding="utf-8") as fh:
        return yaml, yaml.load(fh)


def _save_yaml(yaml, data, path: Path) -> None:
    with path.open("w", encoding="utf-8") as fh:
        yaml.dump(data, fh)


def list_coordinates(appsettings_path: Path) -> None:
    if not appsettings_path.exists():
        print(f"Ficheiro não encontrado: {appsettings_path}", file=sys.stderr)
        raise SystemExit(1)

    _, data = _load_yaml(appsettings_path)
    coords = data.get("coordinates", {})
    if not coords:
        print("Nenhuma coordenada encontrada em 'coordinates:'.")
        return

    print(f"{'nome':35s} x      y")
    print("-" * 50)
    for name, point in coords.items():
        print(f"{name:35s} {point['x']:<6} {point['y']}")


def capture_coordinates(appsettings_path: Path, only: list[str] | None) -> None:
    import pyautogui

    if not appsettings_path.exists():
        print(f"Ficheiro não encontrado: {appsettings_path}", file=sys.stderr)
        raise SystemExit(1)

    yaml, data = _load_yaml(appsettings_path)
    coords = data.get("coordinates")
    if not coords:
        print("O appsettings não tem nenhuma secção 'coordinates:' para calibrar.", file=sys.stderr)
        raise SystemExit(1)

    names = only or list(coords.keys())
    unknown = [n for n in names if n not in coords]
    if unknown:
        print(f"Nomes desconhecidos (não existem em 'coordinates:'): {', '.join(unknown)}", file=sys.stderr)
        raise SystemExit(1)

    print(f"A calibrar {len(names)} coordenada(s). Para cada uma:")
    print("  1. Posicione o rato exatamente sobre o elemento na interface do CMS")
    print("  2. Volte a esta janela e pressione Enter\n")

    captured: dict[str, tuple[int, int]] = {}
    for name in names:
        old = coords[name]
        input(f"[{name}] (atual: {old['x']}, {old['y']}) — posicione o rato e pressione Enter...")
        x, y = pyautogui.position()
        captured[name] = (x, y)
        print(f"  -> capturado: ({x}, {y})\n")

    print("Resumo das novas coordenadas:")
    print(f"{'nome':35s} {'antes':15s} depois")
    print("-" * 65)
    for name, (x, y) in captured.items():
        old = coords[name]
        print(f"{name:35s} ({old['x']}, {old['y']})".ljust(51) + f"({x}, {y})")

    resposta = input("\nGravar estas coordenadas em "
                      f"{appsettings_path}? [s/N] ").strip().lower()
    if resposta != "s":
        print("Nada foi gravado.")
        return

    for name, (x, y) in captured.items():
        coords[name]["x"] = x
        coords[name]["y"] = y

    _save_yaml(yaml, data, appsettings_path)
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
