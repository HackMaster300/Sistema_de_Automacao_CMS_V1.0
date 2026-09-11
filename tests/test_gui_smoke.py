"""Testes de fumaça da GUI.

Usam um Tkinter real (não mockado) para apanhar o tipo de erro que só
aparece ao correr de verdade — como o bug encontrado durante o
desenvolvimento (ler uma tk.Variable de dentro da thread de trabalho).
Se não houver display disponível (`DISPLAY` não definido / Tk não
consegue abrir uma janela), os testes são saltados em vez de falhar —
útil em CI sem Xvfb configurado.
"""
from __future__ import annotations

import time

import pytest

tk = pytest.importorskip("tkinter")

try:
    _root_probe = tk.Tk()
    _root_probe.destroy()
    _HAS_DISPLAY = True
except tk.TclError:
    _HAS_DISPLAY = False

pytestmark = pytest.mark.skipif(not _HAS_DISPLAY, reason="Sem display Tkinter disponível")


def _pump(root, seconds: float = 2.0, step: float = 0.1) -> None:
    elapsed = 0.0
    while elapsed < seconds:
        root.update()
        time.sleep(step)
        elapsed += step


def _write_sample_csv(path):
    path.write_text(
        "identificador,estado,processado_em\n"
        "00000000001,pendente,\n"
        "00000000002,pendente,\n"
    )


@pytest.fixture
def app_and_root(tmp_path):
    from cms_automation.gui.app import CmsAutomationApp

    appsettings_path = tmp_path / "appsettings.yaml"
    appsettings_path.write_text(
        """
dry_run: false
require_confirmation_for_fraud_flag: true
data_file: "dados.csv"
log_dir: "logs"
ocr:
  tesseract_cmd: "auto"
  ocr_region: { x: 0, y: 0, width: 10, height: 10 }
  confirmation_region: { x: 0, y: 0, width: 10, height: 10 }
error_templates:
  primary: "a.png"
  secondary: "b.png"
  tertiary: "c.png"
coordinates:
  campo_pf: { x: 1, y: 1 }
  botao_contador: { x: 1, y: 1 }
  botao_ok_erro: { x: 1, y: 1 }
  area_clique_confirmacao: { x: 1, y: 1 }
  botao_seguinte: { x: 1, y: 1 }
  botao_processamento: { x: 1, y: 1 }
  botao_processamento_seguinte: { x: 1, y: 1 }
  botao_imprimir: { x: 1, y: 1 }
  botao_processamento_sim: { x: 1, y: 1 }
  botao_registado: { x: 1, y: 1 }
  botao_registado_seguinte: { x: 1, y: 1 }
  campo_registado_cmp1: { x: 1, y: 1 }
  campo_potencia: { x: 1, y: 1 }
  campo_propriedade: { x: 1, y: 1 }
  campo_gis_x: { x: 1, y: 1 }
  campo_gis_y: { x: 1, y: 1 }
  campo_estado_instalacao: { x: 1, y: 1 }
  campo_num_luz: { x: 1, y: 1 }
  campo_quartos: { x: 1, y: 1 }
  botao_registro: { x: 1, y: 1 }
  botao_registado_sim: { x: 1, y: 1 }
  botao_anterior: { x: 1, y: 1 }
form_defaults: {}
timing: {}
"""
    )

    root = tk.Tk()
    app = CmsAutomationApp(root)
    yield app, root, tmp_path
    root.destroy()


def test_dry_run_completes_and_updates_stats_label(app_and_root):
    app, root, tmp_path = app_and_root
    data_path = tmp_path / "dados.csv"
    _write_sample_csv(data_path)

    app.appsettings_path.set(str(tmp_path / "appsettings.yaml"))
    app.data_path.set(str(data_path))
    app.dry_run.set(True)

    app._start()
    _pump(root)

    assert "Total processado: 2" in app.stats_label.cget("text")
    assert str(app.start_button.cget("state")) == "normal"
    assert str(app.cancel_button.cget("state")) == "disabled"


def test_cancel_before_processing_leaves_all_records_pending(app_and_root):
    app, root, tmp_path = app_and_root
    data_path = tmp_path / "dados.csv"
    _write_sample_csv(data_path)

    app.appsettings_path.set(str(tmp_path / "appsettings.yaml"))
    app.data_path.set(str(data_path))
    app.dry_run.set(True)

    app._start()
    app._cancel()
    _pump(root)

    assert "Total processado: 0" in app.stats_label.cget("text")
    assert "pendente" in data_path.read_text()
    assert "concluido" not in data_path.read_text()
    assert "erro" not in data_path.read_text()


def test_log_entries_flow_into_widget(app_and_root):
    app, root, tmp_path = app_and_root
    data_path = tmp_path / "dados.csv"
    _write_sample_csv(data_path)

    app.appsettings_path.set(str(tmp_path / "appsettings.yaml"))
    app.data_path.set(str(data_path))
    app.dry_run.set(True)

    app._start()
    _pump(root)

    log_content = app.log_text.get("1.0", "end")
    assert "Automação" in log_content


def test_calibration_window_opens_and_lists_coordinates(app_and_root):
    app, root, tmp_path = app_and_root
    app.appsettings_path.set(str(tmp_path / "appsettings.yaml"))

    app._open_calibration_window()
    root.update()

    toplevels = [w for w in root.winfo_children() if isinstance(w, tk.Toplevel)]
    assert len(toplevels) == 1


def test_missing_appsettings_shows_error_not_crash(app_and_root, monkeypatch):
    app, root, tmp_path = app_and_root
    app.appsettings_path.set(str(tmp_path / "nao_existe.yaml"))
    app.data_path.set(str(tmp_path / "dados.csv"))

    # Evita que messagebox real bloqueie o teste à espera de clique
    from tkinter import messagebox

    shown = {}
    monkeypatch.setattr(
        messagebox, "showerror", lambda title, msg: shown.setdefault("msg", msg)
    )

    app._start()

    assert "msg" in shown
    assert app.worker_thread is None
