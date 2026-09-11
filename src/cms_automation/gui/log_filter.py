"""Filtragem de entradas de log por data e categoria.

Extraído da GUI original (que misturava esta lógica com a construção
da janela de filtros) para ser testável sem Tkinter.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass(frozen=True)
class LogEntry:
    timestamp: datetime
    category: str
    message: str

    def format_line(self) -> str:
        ts = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        return f"[{ts}] [{self.category}] {self.message}"


def filter_log_entries(
    entries: list[LogEntry],
    start_date: datetime,
    end_date: datetime,
    categories: set[str],
) -> list[LogEntry]:
    """Devolve as entradas dentro de [start_date, end_date] (inclusive,
    até ao fim do dia de end_date) e cuja categoria esteja em `categories`."""
    end_inclusive = end_date + timedelta(days=1)
    return [
        entry
        for entry in entries
        if start_date <= entry.timestamp < end_inclusive and entry.category in categories
    ]


def parse_date(date_str: str) -> datetime:
    """Lança ValueError com mensagem clara se o formato não for YYYY-MM-DD."""
    try:
        return datetime.strptime(date_str.strip(), "%Y-%m-%d")
    except ValueError as exc:
        raise ValueError(f"Formato de data inválido: '{date_str}'. Use YYYY-MM-DD.") from exc
