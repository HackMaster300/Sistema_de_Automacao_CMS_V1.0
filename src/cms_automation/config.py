"""Carregamento e validação da configuração da automação.

Toda coordenada de ecrã, caminho de imagem, e parâmetro de tempo vive num
ficheiro YAML externo (ver config/appsettings.example.yaml). O código nunca
deve conter coordenadas ou caminhos fixos — isso é o que tornava o V1.0
impossível de manter fora da máquina original do autor.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


class ConfigError(Exception):
    """Erro de configuração inválida ou em falta."""


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def as_tuple(self) -> tuple[int, int]:
        return (self.x, self.y)


@dataclass(frozen=True)
class Region:
    x: int
    y: int
    width: int
    height: int

    def as_tuple(self) -> tuple[int, int, int, int]:
        return (self.x, self.y, self.width, self.height)


@dataclass(frozen=True)
class Timing:
    short_pause: float = 0.2
    click_pause: float = 0.5
    ocr_settle_pause: float = 1.0
    error_check_pause: float = 1.0


@dataclass(frozen=True)
class OcrSettings:
    tesseract_cmd: str
    ocr_region: Region
    confirmation_region: Region


@dataclass(frozen=True)
class ErrorTemplates:
    primary: Path
    secondary: Path
    tertiary: Path
    confidence_primary: float = 0.7
    confidence_secondary: float = 0.5
    confidence_tertiary: float = 0.7


@dataclass(frozen=True)
class Coordinates:
    """Todas as coordenadas de UI usadas pela automação, nomeadas."""
    points: dict[str, Point]

    def get(self, name: str) -> Point:
        try:
            return self.points[name]
        except KeyError as exc:
            raise ConfigError(
                f"Coordenada '{name}' não definida em config.yaml -> coordinates"
            ) from exc


@dataclass(frozen=True)
class FormDefaults:
    """Valores usados para preencher os campos do formulário de registo.

    No V1.0 estes valores eram teclas soltas ('r', '2', '4', ...)
    espalhadas por centenas de linhas, sem nome nem explicação. Aqui
    cada um tem uma chave legível e vive num ficheiro de configuração
    versionável e revisável — ajuste-os para refletir o seu ambiente
    real (idealmente, no futuro, lidos diretamente da base de dados do
    contador em vez de fixos).
    """
    values: dict[str, str]

    def get(self, key: str) -> str:
        try:
            return self.values[key]
        except KeyError as exc:
            raise ConfigError(
                f"Valor de formulário '{key}' não definido em config.yaml -> form_defaults"
            ) from exc


@dataclass(frozen=True)
class AppConfig:
    tesseract_cmd: str
    ocr: OcrSettings
    error_templates: ErrorTemplates
    coordinates: Coordinates
    timing: Timing
    form_defaults: FormDefaults
    data_file: Path
    log_dir: Path
    require_confirmation_for_fraud_flag: bool = True
    dry_run: bool = False


def _point(d: dict[str, Any]) -> Point:
    return Point(int(d["x"]), int(d["y"]))


def _region(d: dict[str, Any]) -> Region:
    return Region(int(d["x"]), int(d["y"]), int(d["width"]), int(d["height"]))


def load_config(path: str | Path) -> AppConfig:
    """Lê e valida um ficheiro YAML de configuração.

    Lança ConfigError com uma mensagem clara se algo essencial faltar,
    em vez de falhar a meio da execução com um KeyError críptico.
    """
    path = Path(path)
    if not path.exists():
        raise ConfigError(
            f"Ficheiro de configuração não encontrado: {path}\n"
            "Copie config/appsettings.example.yaml para config/appsettings.yaml e "
            "ajuste os valores para o seu ambiente."
        )

    with path.open("r", encoding="utf-8") as fh:
        raw = yaml.safe_load(fh) or {}

    try:
        coords_raw = raw["coordinates"]
        coordinates = Coordinates(
            points={name: _point(v) for name, v in coords_raw.items()}
        )

        ocr_raw = raw["ocr"]
        ocr = OcrSettings(
            tesseract_cmd=ocr_raw["tesseract_cmd"],
            ocr_region=_region(ocr_raw["ocr_region"]),
            confirmation_region=_region(ocr_raw["confirmation_region"]),
        )

        err_raw = raw["error_templates"]
        base_dir = path.parent
        error_templates = ErrorTemplates(
            primary=(base_dir / err_raw["primary"]).resolve(),
            secondary=(base_dir / err_raw["secondary"]).resolve(),
            tertiary=(base_dir / err_raw["tertiary"]).resolve(),
            confidence_primary=float(err_raw.get("confidence_primary", 0.7)),
            confidence_secondary=float(err_raw.get("confidence_secondary", 0.5)),
            confidence_tertiary=float(err_raw.get("confidence_tertiary", 0.7)),
        )

        timing_raw = raw.get("timing", {})
        timing = Timing(**{k: float(v) for k, v in timing_raw.items()})

        data_file = (path.parent / raw["data_file"]).resolve()
        log_dir = (path.parent / raw.get("log_dir", "../logs")).resolve()

        form_defaults = FormDefaults(
            values={k: str(v) for k, v in raw.get("form_defaults", {}).items()}
        )

    except KeyError as exc:
        raise ConfigError(f"Chave obrigatória em falta em {path}: {exc}") from exc

    return AppConfig(
        tesseract_cmd=ocr.tesseract_cmd,
        ocr=ocr,
        error_templates=error_templates,
        coordinates=coordinates,
        timing=timing,
        form_defaults=form_defaults,
        data_file=data_file,
        log_dir=log_dir,
        require_confirmation_for_fraud_flag=bool(
            raw.get("require_confirmation_for_fraud_flag", True)
        ),
        dry_run=bool(raw.get("dry_run", False)),
    )
