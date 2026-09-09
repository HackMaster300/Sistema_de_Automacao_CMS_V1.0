"""Logging estruturado (consola + ficheiro), substituindo os `print`
espalhados pelo V1.0 — importante para auditoria, já que este sistema
altera registos num CMS de produção."""
from __future__ import annotations

import logging
import sys
import time
from pathlib import Path


def setup_logging(log_dir: str | Path, level: int = logging.INFO) -> Path:
    log_dir = Path(log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / f"cms_automation_{time.strftime('%Y%m%d_%H%M%S')}.log"

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

    root = logging.getLogger()
    root.setLevel(level)
    root.handlers.clear()

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)
    root.addHandler(file_handler)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    root.addHandler(console_handler)

    return log_file
