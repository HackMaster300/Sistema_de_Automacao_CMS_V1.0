"""Ponte entre o `logging` do núcleo e a interface gráfica.

A automação corre numa thread de fundo (para a janela não travar). O
logging do Python já é thread-safe para escrever, mas os widgets do
Tkinter só podem ser tocados a partir da thread principal — por isso
este handler só *acumula* entradas numa fila; é a GUI, a partir do loop
principal (`after()`), que as vai buscar e desenha.
"""
from __future__ import annotations

import logging
import queue
from datetime import datetime

from .log_filter import LogEntry


class QueueLogHandler(logging.Handler):
    def __init__(self) -> None:
        super().__init__()
        self.queue: queue.Queue[LogEntry] = queue.Queue()

    def emit(self, record: logging.LogRecord) -> None:
        category = getattr(record, "categoria", None) or record.name.rsplit(".", 1)[-1].capitalize()
        entry = LogEntry(
            timestamp=datetime.fromtimestamp(record.created),
            category=category,
            message=record.getMessage(),
        )
        self.queue.put(entry)

    def drain(self) -> list[LogEntry]:
        """Devolve (e remove da fila) todas as entradas acumuladas desde
        a última chamada. Chamado a partir do loop principal da GUI."""
        entries = []
        while True:
            try:
                entries.append(self.queue.get_nowait())
            except queue.Empty:
                break
        return entries
