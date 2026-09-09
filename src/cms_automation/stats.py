"""Estatísticas de execução — substitui os contadores soltos e os vários
`print(f"...")` espalhados pelo fim do V1.0."""
from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass, field


@dataclass
class ProcessingStats:
    total_processados: int = 0
    contador_introduzido: int = 0
    contador_em_processamento: int = 0
    contador_registados: int = 0
    contador_fraude_pendente_revisao: int = 0
    numeros_errados: int = 0
    started_at: float = field(default_factory=time.time)
    finished_at: float | None = None

    def finish(self) -> None:
        self.finished_at = time.time()

    @property
    def duration_minutes(self) -> float:
        end = self.finished_at or time.time()
        return (end - self.started_at) / 60

    def as_dict(self) -> dict:
        d = asdict(self)
        d["duration_minutes"] = round(self.duration_minutes, 2)
        return d

    def to_json(self, path: str) -> None:
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(self.as_dict(), fh, indent=2, ensure_ascii=False)

    def summary_text(self) -> str:
        d = self.as_dict()
        return (
            "Processo concluído!\n"
            f"Duração total: {d['duration_minutes']:.2f} min\n"
            f"Total processado: {d['total_processados']}\n"
            f"Introduzidos: {d['contador_introduzido']}\n"
            f"Em processamento: {d['contador_em_processamento']}\n"
            f"Registados: {d['contador_registados']}\n"
            f"Pendentes de revisão (suspeita de fraude): "
            f"{d['contador_fraude_pendente_revisao']}\n"
            f"Erros detetados: {d['numeros_errados']}"
        )
