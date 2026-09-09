"""Conversão do texto bruto extraído por OCR em registos estruturados.

No V1.0 esta lógica estava duplicada quatro vezes ao longo do ficheiro
(uma por cada variação no número de linhas detetadas pelo OCR), cada
cópia com pequenas divergências. Aqui existe um único caminho, testável
sem qualquer ecrã real.
"""
from __future__ import annotations

import re

from .workflow.states import ParsedRecord, RecordState

_OT_PATTERN = re.compile(r"^\d+")
_FRAUD_KEYWORD = "suspeita de fraude"


def split_lines(texto_extraido: str) -> list[str]:
    """Divide o texto do OCR em linhas não vazias, sem espaços extra."""
    return [linha.strip() for linha in texto_extraido.split("\n") if linha.strip()]


def combine_ocr_columns(linhas: list[str]) -> list[str]:
    """Recombina colunas que o OCR devolve como blocos separados.

    A tabela do CMS é lida pelo OCR como três blocos verticais
    (tipo / estado / centro) em vez de uma linha por registo. Quando o
    número de linhas é múltiplo de três, reconstruímos cada linha lógica
    juntando a entrada correspondente de cada bloco.

    Quando o número de linhas NÃO é múltiplo de três (ex: exatamente 3
    linhas, ou uma captura irregular), assume-se que o OCR já devolveu
    uma linha por registo e nenhuma recombinação é necessária.
    """
    if len(linhas) == 0:
        return []

    if len(linhas) % 3 != 0:
        return linhas

    total_grupos = len(linhas) // 3
    tipos = linhas[:total_grupos]
    estados = linhas[total_grupos: 2 * total_grupos]
    centros = linhas[2 * total_grupos:]

    return [
        f"{tipos[i]} {estados[i]} {centros[i]}".strip()
        for i in range(total_grupos)
    ]


def parse_record(line_index: int, linha: str) -> ParsedRecord:
    match = _OT_PATTERN.match(linha)
    ot_number = match.group() if match else None

    return ParsedRecord(
        raw_line=linha,
        ot_number=ot_number,
        state=RecordState.from_text(linha),
        flagged_for_fraud_review=_FRAUD_KEYWORD in linha.lower(),
        line_index=line_index,
    )


def parse_ocr_text(texto_extraido: str) -> list[ParsedRecord]:
    """Pipeline completo: texto OCR bruto -> lista de ParsedRecord."""
    linhas = split_lines(texto_extraido)
    linhas_combinadas = combine_ocr_columns(linhas)
    return [parse_record(i, linha) for i, linha in enumerate(linhas_combinadas)]
