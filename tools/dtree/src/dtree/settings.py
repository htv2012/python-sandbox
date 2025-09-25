import pathlib
import tomllib

DEFAULT_SETTINGS = """
[color]
key = "bright_blue"
string = "bright_yellow"
non_string = "bright_cyan"
error = "red"
""".strip()


def load(config_path: pathlib.Path = None) -> dict:
    if config_path is None:
        config_path = pathlib.Path("~/.config/dtree.toml").expanduser()
    if not config_path.exists():
        config_path.write_text(DEFAULT_SETTINGS)

    config_text = config_path.read_text()
    config = tomllib.loads(config_text)
    return config
