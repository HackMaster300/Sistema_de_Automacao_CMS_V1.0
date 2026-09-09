import pytest

from cms_automation.config import ConfigError, load_config


def test_load_config_never_creates_missing_appsettings(tmp_path):
    """appsettings.yaml tem de já existir — load_config nunca cria um
    ficheiro novo, só lê um existente. Erra com uma mensagem clara em
    vez de arrancar com valores vazios/adivinhados."""
    path = tmp_path / "appsettings.yaml"

    with pytest.raises(ConfigError):
        load_config(path)

    assert not path.exists()


def test_load_config_error_message_points_to_example_file(tmp_path):
    path = tmp_path / "appsettings.yaml"
    with pytest.raises(ConfigError) as exc_info:
        load_config(path)

    assert "config.example.yaml" in str(exc_info.value) or "appsettings.example.yaml" in str(exc_info.value)
