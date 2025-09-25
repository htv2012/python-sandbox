from dtree import settings


def test_load_with_path(tmp_path):
    config_path = tmp_path / "data.toml"
    config_path.write_text('[color]\nkey="black"')
    config = settings.load(config_path)
    assert config == {"color": {"key": "black"}}
