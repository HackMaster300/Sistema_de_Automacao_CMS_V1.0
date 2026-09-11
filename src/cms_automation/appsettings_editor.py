"""Leitura e escrita do appsettings.yaml preservando comentários.

Usado tanto por `tools/calibrate_coordinates.py` (CLI) como pela GUI —
para não haver duas implementações da mesma coisa, esta é a única.
Depende de `ruamel.yaml` (extra opcional "calibration"), importado só
aqui dentro, nunca a partir do núcleo do pacote.
"""
from __future__ import annotations

from pathlib import Path


class AppsettingsEditError(Exception):
    pass


def load_editable(path: Path):
    """Devolve (yaml, data) — data é um dict "vivo": editar e passar de
    volta a save_editable() preserva comentários e formatação."""
    from ruamel.yaml import YAML

    if not path.exists():
        raise AppsettingsEditError(f"Ficheiro não encontrado: {path}")

    yaml = YAML()
    yaml.preserve_quotes = True
    with path.open("r", encoding="utf-8") as fh:
        data = yaml.load(fh)
    return yaml, data


def save_editable(yaml, data, path: Path) -> None:
    with path.open("w", encoding="utf-8") as fh:
        yaml.dump(data, fh)


def list_coordinate_names(data) -> list[str]:
    coords = data.get("coordinates") or {}
    return list(coords.keys())


def get_coordinate(data, name: str) -> tuple[int, int]:
    coords = data.get("coordinates") or {}
    if name not in coords:
        raise AppsettingsEditError(f"Coordenada '{name}' não existe em 'coordinates:'.")
    point = coords[name]
    return int(point["x"]), int(point["y"])


def update_coordinate(data, name: str, x: int, y: int) -> None:
    coords = data.get("coordinates") or {}
    if name not in coords:
        raise AppsettingsEditError(f"Coordenada '{name}' não existe em 'coordinates:'.")
    coords[name]["x"] = x
    coords[name]["y"] = y
