import csv
import threading

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
from cms_automation.data_source import CsvDataSource, RecordStatus
from cms_automation.input.fake_controller import FakeInputController
from cms_automation.stats import ProcessingStats
from cms_automation.vision.fake_backend import FakeVisionBackend
from cms_automation.workflow.processor import process_batch
from pathlib import Path


def _minimal_config() -> AppConfig:
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
    )


def test_cancel_event_stops_before_next_identifier(tmp_path):
    path = tmp_path / "dados.csv"
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["identificador", "estado", "processado_em"])
        writer.writerows([["1111", "pendente", ""], ["2222", "pendente", ""], ["3333", "pendente", ""]])

    data_source = CsvDataSource(path)
    config = _minimal_config()
    input_ctrl = FakeInputController()
    vision = FakeVisionBackend()

    cancel_event = threading.Event()
    cancel_event.set()  # já cancelado antes de começar

    stats = process_batch(data_source, config, input_ctrl, vision, cancel_event=cancel_event)

    assert stats.total_processados == 0
    # Nenhum registo foi tocado — todos continuam pendentes
    assert [r.estado for r in data_source.load_all()] == [RecordStatus.PENDENTE] * 3


def test_without_cancel_event_processes_normally(tmp_path):
    path = tmp_path / "dados.csv"
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["identificador", "estado", "processado_em"])
        writer.writerows([["1111", "pendente", ""]])

    data_source = CsvDataSource(path)
    config = _minimal_config()
    stats = process_batch(
        data_source, config, FakeInputController(), FakeVisionBackend(), cancel_event=None
    )
    assert stats.total_processados == 1
