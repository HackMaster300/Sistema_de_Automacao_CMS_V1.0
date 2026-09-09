from pathlib import Path

import pytest

from cms_automation.vision.tesseract_locator import (
    TesseractNotFoundError,
    resolve_tesseract_cmd,
)


def test_explicit_path_is_returned_unchanged():
    assert resolve_tesseract_cmd("/caminho/manual/tesseract") == "/caminho/manual/tesseract"


def test_auto_finds_bundled_copy_next_to_executable(tmp_path, monkeypatch):
    bundled = tmp_path / "tesseract"
    bundled.mkdir()
    (bundled / "tesseract").write_text("fake binary")

    monkeypatch.setattr(
        "cms_automation.vision.tesseract_locator._executable_dir", lambda: tmp_path
    )
    # Garante que não encontra nada no PATH, para isolar o teste ao caso "bundled"
    monkeypatch.setattr("shutil.which", lambda name: None)

    resolved = resolve_tesseract_cmd("auto")
    assert resolved == str(bundled / "tesseract")


def test_auto_falls_back_to_system_path(tmp_path, monkeypatch):
    monkeypatch.setattr(
        "cms_automation.vision.tesseract_locator._executable_dir", lambda: tmp_path
    )
    monkeypatch.setattr("shutil.which", lambda name: "/usr/bin/tesseract")

    assert resolve_tesseract_cmd("auto") == "/usr/bin/tesseract"


def test_auto_raises_clear_error_when_nothing_found(tmp_path, monkeypatch):
    monkeypatch.setattr(
        "cms_automation.vision.tesseract_locator._executable_dir", lambda: tmp_path
    )
    monkeypatch.setattr("shutil.which", lambda name: None)
    monkeypatch.setattr(
        "cms_automation.vision.tesseract_locator._COMMON_PATHS", []
    )

    with pytest.raises(TesseractNotFoundError):
        resolve_tesseract_cmd("auto")


def test_auto_is_case_insensitive(tmp_path, monkeypatch):
    monkeypatch.setattr(
        "cms_automation.vision.tesseract_locator._executable_dir", lambda: tmp_path
    )
    monkeypatch.setattr("shutil.which", lambda name: "/usr/bin/tesseract")

    assert resolve_tesseract_cmd("AUTO") == "/usr/bin/tesseract"
