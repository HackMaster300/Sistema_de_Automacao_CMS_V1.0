from cms_automation.parsing import combine_ocr_columns, parse_ocr_text, split_lines
from cms_automation.workflow.states import RecordState


def test_split_lines_removes_blank_and_strips():
    texto = "  linha 1  \n\n linha 2\n"
    assert split_lines(texto) == ["linha 1", "linha 2"]


def test_combine_ocr_columns_recombines_three_blocks():
    # 2 registos, cada bloco (tipo/estado/centro) com 2 linhas
    linhas = ["TipoA", "TipoB", "Registado", "Em processamento", "CentroA", "CentroB"]
    combinadas = combine_ocr_columns(linhas)
    assert combinadas == ["TipoA Registado CentroA", "TipoB Em processamento CentroB"]


def test_combine_ocr_columns_passthrough_when_not_multiple_of_three():
    linhas = ["1234 Registado suspeita de fraude"]
    assert combine_ocr_columns(linhas) == linhas


def test_parse_ocr_text_identifies_registado_state():
    texto = "1234 Registado suspeita de fraude\n"
    records = parse_ocr_text(texto)
    assert len(records) == 1
    assert records[0].state is RecordState.REGISTADO
    assert records[0].ot_number == "1234"
    assert records[0].flagged_for_fraud_review is True


def test_parse_ocr_text_identifies_em_processamento_state():
    texto = "5678 Em processamento normal\n"
    records = parse_ocr_text(texto)
    assert records[0].state is RecordState.EM_PROCESSAMENTO
    assert records[0].flagged_for_fraud_review is False


def test_parse_ocr_text_defaults_to_introduzido():
    texto = "9999 Introduzido\n"
    records = parse_ocr_text(texto)
    assert records[0].state is RecordState.INTRODUZIDO


def test_parse_ocr_text_handles_empty_input():
    assert parse_ocr_text("") == []
