from datetime import datetime

import pytest

from cms_automation.gui.log_filter import LogEntry, filter_log_entries, parse_date


def _entry(day: str, category: str, message: str = "msg") -> LogEntry:
    return LogEntry(timestamp=datetime.strptime(day, "%Y-%m-%d"), category=category, message=message)


def test_filter_by_category():
    entries = [_entry("2026-01-01", "Automação"), _entry("2026-01-01", "Captura")]
    result = filter_log_entries(
        entries,
        start_date=datetime(2026, 1, 1),
        end_date=datetime(2026, 1, 31),
        categories={"Automação"},
    )
    assert len(result) == 1
    assert result[0].category == "Automação"


def test_filter_by_date_range_is_inclusive_of_end_day():
    entries = [_entry("2026-01-05", "Geral"), _entry("2026-01-10", "Geral"), _entry("2026-01-15", "Geral")]
    result = filter_log_entries(
        entries,
        start_date=datetime(2026, 1, 5),
        end_date=datetime(2026, 1, 10),
        categories={"Geral"},
    )
    assert len(result) == 2


def test_parse_date_valid():
    assert parse_date("2026-01-01") == datetime(2026, 1, 1)


def test_parse_date_invalid_raises_clear_error():
    with pytest.raises(ValueError, match="YYYY-MM-DD"):
        parse_date("01/01/2026")


def test_format_line():
    entry = _entry("2026-01-01", "Automação", "processando 1234")
    assert entry.format_line() == "[2026-01-01 00:00:00] [Automação] processando 1234"
