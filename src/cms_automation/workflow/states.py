"""Estados possíveis de um registo, tal como reportados pelo sistema CMS."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class RecordState(str, Enum):
    """Estado de uma inspeção/registo identificado a partir do texto OCR.

    Corresponde diretamente às strings que o sistema legado mostra na
    interface: "Registado", "Em processamento", ou nenhuma keyword
    reconhecida (tratado como "Introduzido" / fluxo padrão).
    """

    REGISTADO = "registado"
    EM_PROCESSAMENTO = "em_processamento"
    INTRODUZIDO = "introduzido"

    @classmethod
    def from_text(cls, texto: str) -> "RecordState":
        texto_lower = texto.lower()
        if "registad" in texto_lower:
            return cls.REGISTADO
        if "em processamento" in texto_lower:
            return cls.EM_PROCESSAMENTO
        return cls.INTRODUZIDO


@dataclass(frozen=True)
class ParsedRecord:
    """Uma linha da tabela OCR já interpretada."""

    raw_line: str
    ot_number: str | None
    state: RecordState
    flagged_for_fraud_review: bool
    line_index: int
