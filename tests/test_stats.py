from cms_automation.stats import ProcessingStats


def test_stats_defaults_are_zero():
    stats = ProcessingStats()
    assert stats.total_processados == 0
    assert stats.contador_fraude_pendente_revisao == 0


def test_stats_finish_sets_finished_at_and_duration():
    stats = ProcessingStats()
    stats.finish()
    assert stats.finished_at is not None
    assert stats.duration_minutes >= 0


def test_summary_text_includes_counters():
    stats = ProcessingStats(total_processados=5, contador_registados=2)
    stats.finish()
    text = stats.summary_text()
    assert "Total processado: 5" in text
    assert "Registados: 2" in text
