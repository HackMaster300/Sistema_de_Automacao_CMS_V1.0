"""Receitas (sequências de Step) para cada estado de registo.

No V1.0, os estados "Registado" e "Em processamento" executavam a
*mesma* sequência de preenchimento (confirmado por diff byte-a-byte
entre os dois blocos do ficheiro original) — só o "Introduzido"
(nenhuma keyword reconhecida) tinha um caminho diferente, que não fazia
mais do que contar o registo. Por isso existe aqui uma única receita de
registo, partilhada pelos dois estados.
"""
from __future__ import annotations

from ..config import FormDefaults
from .steps import Step, StepKind


def build_registration_steps(defaults: FormDefaults) -> list[Step]:
    """Sequência de preenchimento do formulário técnico do registo.

    Os valores literais (fd.get(...)) vêm de config.yaml -> form_defaults,
    documentados lá com o significado de cada campo no seu ambiente.
    """
    fd = defaults
    return [
        Step(StepKind.CLICK, coordinate="campo_registado_cmp1"),
        Step(StepKind.TYPE_THEN_TAB, value=fd.get("header_type_code")),
        Step(StepKind.TYPE_THEN_TAB, value=fd.get("header_subtype_code")),
        Step(StepKind.TYPE_THEN_TAB, value=fd.get("header_value_1")),
        Step(StepKind.KEY, value="shift+tab"),
        Step(StepKind.SLEEP, seconds=2.0),
        Step(
            StepKind.OCR_CHECK,
            region="confirmation_region",
            expected_text=fd.get("confirmation_expected_text"),
            extra_key_if_match=fd.get("confirmation_match_extra_key"),
        ),
        Step(StepKind.KEY, value="tab"),
        Step(StepKind.TYPE_THEN_TAB, value=fd.get("status_flag_1")),
        Step(StepKind.TYPE_THEN_TAB, value=fd.get("status_flag_2")),
        Step(StepKind.TYPE_THEN_TAB, value=fd.get("block_code_a")),
        Step(StepKind.TYPE_THEN_TAB, value=fd.get("block_code_year")),
        Step(StepKind.TYPE_THEN_TAB, value=fd.get("block_code_month")),
        Step(StepKind.TYPE_THEN_TAB, value=fd.get("block_code_day")),
        Step(StepKind.TYPE_THEN_TAB, value=fd.get("block_code_year_2")),
        Step(StepKind.CLICK, coordinate="campo_potencia"),
        Step(StepKind.TYPE_THEN_TAB, value=fd.get("power_rating")),
        Step(StepKind.CLICK, coordinate="campo_propriedade", clicks=2),
        Step(StepKind.KEY, value="backspace"),
        Step(StepKind.TYPE_THEN_TAB, value=fd.get("property_code")),
        Step(StepKind.CLICK, coordinate="campo_gis_x", clicks=2),
        Step(StepKind.KEY, value="backspace"),
        Step(StepKind.KEY, value=fd.get("gis_x_offset")),
        Step(StepKind.CLICK, coordinate="campo_gis_y", clicks=2),
        Step(StepKind.KEY, value="backspace"),
        Step(StepKind.KEY, value=fd.get("gis_y_offset")),
        Step(StepKind.CLICK, coordinate="campo_estado_instalacao"),
        Step(StepKind.TYPE_THEN_TAB, value=fd.get("installation_state_flag")),
        Step(StepKind.TYPE_THEN_TAB, value=fd.get("installation_state_flag")),
        Step(StepKind.TYPE_THEN_TAB, value=fd.get("installation_state_flag")),
        Step(StepKind.KEY, value=fd.get("installation_state_flag")),
        Step(StepKind.CLICK, coordinate="campo_num_luz"),
        Step(StepKind.KEY, value=fd.get("meter_last_digit")),
        Step(StepKind.SLEEP, seconds=1.0),
        Step(StepKind.CLICK, coordinate="campo_quartos"),
        Step(StepKind.KEY, value=fd.get("rooms_count")),
        Step(StepKind.CLICK, coordinate="botao_registro"),
        Step(StepKind.KEY, value="space"),
        Step(StepKind.KEY, value="space"),
        Step(StepKind.KEY, value="space"),
        Step(StepKind.KEY, value="tab"),
        Step(StepKind.KEY, value=fd.get("finalize_flag")),
        Step(StepKind.CLICK, coordinate="botao_registado_sim"),
        Step(StepKind.KEY, value="space"),
        Step(StepKind.KEY, value="space"),
        Step(StepKind.KEY, value="space"),
        Step(StepKind.CLICK, coordinate="botao_anterior", clicks=3),
    ]


def build_navigate_to_registration_steps() -> list[Step]:
    """Passos de navegação até ao ecrã de preenchimento, comuns aos dois
    estados que levam a registo (Registado / Em processamento)."""
    return [
        Step(StepKind.CLICK, coordinate="botao_seguinte", clicks=2),
        Step(StepKind.SLEEP, seconds=1.0),
    ]
