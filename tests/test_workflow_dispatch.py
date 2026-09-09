from pathlib import Path

from cms_automation.config import (
    AppConfig,
    Coordinates,
    ErrorTemplates,
    FormDefaults,
    OcrSettings,
    Point,
    Region,
    Timing,
)
from cms_automation.input.fake_controller import FakeInputController
from cms_automation.vision.fake_backend import FakeVisionBackend
from cms_automation.stats import ProcessingStats
from cms_automation.workflow.processor import dispatch_record
from cms_automation.workflow.states import ParsedRecord, RecordState
from cms_automation.workflow.steps import StepRunner


def _minimal_config(require_confirmation: bool = True) -> AppConfig:
    coord_names = [
        "campo_pf", "botao_contador", "botao_ok_erro", "area_clique_confirmacao",
        "botao_seguinte", "botao_processamento", "botao_processamento_seguinte",
        "botao_imprimir", "botao_processamento_sim", "botao_registado",
        "botao_registado_seguinte", "campo_registado_cmp1", "campo_potencia",
        "campo_propriedade", "campo_gis_x", "campo_gis_y",
        "campo_estado_instalacao", "campo_num_luz", "campo_quartos",
        "botao_registro", "botao_registado_sim", "botao_anterior",
    ]
    coordinates = Coordinates(points={name: Point(0, 0) for name in coord_names})

    form_defaults = FormDefaults(values={
        "header_type_code": "r", "header_subtype_code": "v", "header_value_1": "2",
        "confirmation_expected_text": "22000 V", "confirmation_match_extra_key": "2",
        "status_flag_1": "s", "status_flag_2": "s", "block_code_a": "r",
        "block_code_year": "200", "block_code_month": "43", "block_code_day": "4",
        "block_code_year_2": "200", "power_rating": "2.2", "property_code": "172",
        "gis_x_offset": "2", "gis_y_offset": "1", "installation_state_flag": "s",
        "meter_last_digit": "8", "rooms_count": "4", "finalize_flag": "n",
    })

    region = Region(0, 0, 10, 10)
    return AppConfig(
        tesseract_cmd="/usr/bin/tesseract",
        ocr=OcrSettings(tesseract_cmd="/usr/bin/tesseract", ocr_region=region, confirmation_region=region),
        error_templates=ErrorTemplates(primary=Path("a.png"), secondary=Path("b.png"), tertiary=Path("c.png")),
        coordinates=coordinates,
        timing=Timing(short_pause=0, click_pause=0, ocr_settle_pause=0, error_check_pause=0),
        form_defaults=form_defaults,
        data_file=Path("data.csv"),
        log_dir=Path("logs"),
        require_confirmation_for_fraud_flag=require_confirmation,
    )


def test_fraud_flagged_record_is_not_auto_processed_by_default():
    config = _minimal_config(require_confirmation=True)
    input_ctrl = FakeInputController()
    vision = FakeVisionBackend()
    runner = StepRunner(config, input_ctrl, vision)
    stats = ProcessingStats()

    record = ParsedRecord(
        raw_line="1234 Registado suspeita de fraude",
        ot_number="1234",
        state=RecordState.REGISTADO,
        flagged_for_fraud_review=True,
        line_index=0,
    )

    dispatch_record(record, runner, config, stats)

    assert stats.contador_fraude_pendente_revisao == 1
    assert stats.contador_registados == 0
    assert input_ctrl.actions == []  # nenhuma ação de UI foi executada


def test_registado_record_runs_registration_steps():
    config = _minimal_config()
    input_ctrl = FakeInputController()
    vision = FakeVisionBackend(scripted_texts=["22000 V"])
    runner = StepRunner(config, input_ctrl, vision)
    stats = ProcessingStats()

    record = ParsedRecord(
        raw_line="1234 Registado normal",
        ot_number="1234",
        state=RecordState.REGISTADO,
        flagged_for_fraud_review=False,
        line_index=0,
    )

    dispatch_record(record, runner, config, stats)

    assert stats.contador_registados == 1
    assert len(input_ctrl.actions) > 0


def test_introduzido_record_takes_no_ui_action():
    config = _minimal_config()
    input_ctrl = FakeInputController()
    vision = FakeVisionBackend()
    runner = StepRunner(config, input_ctrl, vision)
    stats = ProcessingStats()

    record = ParsedRecord(
        raw_line="1234 Introduzido",
        ot_number="1234",
        state=RecordState.INTRODUZIDO,
        flagged_for_fraud_review=False,
        line_index=0,
    )

    dispatch_record(record, runner, config, stats)

    assert stats.contador_introduzido == 1
    assert input_ctrl.actions == []
