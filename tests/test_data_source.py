import csv

import pytest

from cms_automation.data_source import (
    CsvDataSource,
    RecordStatus,
    open_data_source,
)


def _write_csv(path, rows):
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["identificador", "estado", "processado_em"])
        writer.writerows(rows)


def test_load_all_defaults_missing_estado_to_pendente(tmp_path):
    path = tmp_path / "dados.csv"
    with path.open("w", encoding="utf-8", newline="") as fh:
        fh.write("identificador\n1234\n5678\n")

    source = CsvDataSource(path)
    records = source.load_all()

    assert len(records) == 2
    assert all(r.estado is RecordStatus.PENDENTE for r in records)


def test_pending_excludes_concluido_and_erro(tmp_path):
    path = tmp_path / "dados.csv"
    _write_csv(
        path,
        [
            ["1111", "pendente", ""],
            ["2222", "concluido", "2026-01-01T10:00:00"],
            ["3333", "erro", "2026-01-01T10:05:00"],
        ],
    )

    source = CsvDataSource(path)
    pendentes = [r.identificador for r in source.pending()]

    assert pendentes == ["1111"]


def test_mark_persists_checkpoint_to_disk(tmp_path):
    path = tmp_path / "dados.csv"
    _write_csv(path, [["1111", "pendente", ""], ["2222", "pendente", ""]])

    source = CsvDataSource(path)
    source.mark("1111", RecordStatus.CONCLUIDO)

    # Recarrega a partir do disco para confirmar que persistiu de verdade
    reloaded = CsvDataSource(path)
    records = {r.identificador: r for r in reloaded.load_all()}

    assert records["1111"].estado is RecordStatus.CONCLUIDO
    assert records["1111"].processado_em is not None
    assert records["2222"].estado is RecordStatus.PENDENTE


def test_resume_only_processes_pending_after_partial_run(tmp_path):
    path = tmp_path / "dados.csv"
    _write_csv(path, [["1111", "pendente", ""], ["2222", "pendente", ""], ["3333", "pendente", ""]])

    source = CsvDataSource(path)
    source.mark("1111", RecordStatus.CONCLUIDO)
    source.mark("2222", RecordStatus.ERRO)

    # Simula um novo processo a arrancar depois de uma interrupção
    resumed_source = CsvDataSource(path)
    pendentes = [r.identificador for r in resumed_source.pending()]

    assert pendentes == ["3333"]


def test_open_data_source_picks_csv_by_extension(tmp_path):
    path = tmp_path / "dados.csv"
    _write_csv(path, [["1111", "pendente", ""]])

    source = open_data_source(path)
    assert isinstance(source, CsvDataSource)


def test_open_data_source_rejects_unknown_extension(tmp_path):
    path = tmp_path / "dados.txt"
    path.write_text("x")

    with pytest.raises(ValueError):
        open_data_source(path)


def test_missing_file_raises_clear_error(tmp_path):
    with pytest.raises(FileNotFoundError):
        CsvDataSource(tmp_path / "nao_existe.csv")


def test_open_data_source_never_creates_missing_csv(tmp_path):
    """Nenhuma fonte de dados cria um ficheiro novo — ele tem de já
    existir. Isto evita rodar um lote silenciosamente contra um
    ficheiro vazio criado por engano."""
    path = tmp_path / "nao_existe.csv"
    with pytest.raises(FileNotFoundError):
        open_data_source(path)
    assert not path.exists()


def test_open_data_source_never_creates_missing_excel(tmp_path):
    path = tmp_path / "nao_existe.xlsx"
    with pytest.raises(FileNotFoundError):
        open_data_source(path)
    assert not path.exists()
