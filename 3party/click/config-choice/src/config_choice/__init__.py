import pathlib

import click

from .config.config_type import ConfigFile, ConfigType

TEST_CONFIG_DIR = pathlib.Path(__file__).parent / "config" / "test_configs"
CONFIG_DIR = pathlib.Path(__file__).parent / "config" / "configs"


@click.command
@click.option(
    "--config", type=ConfigType(cls=ConfigFile, root=CONFIG_DIR), required=True
)
@click.option(
    "--test-config",
    type=ConfigType(root=TEST_CONFIG_DIR),
    default="nightly",
    required=False,
)
def main(config, test_config):
    print(f"Config: {config.name}, config: {config.config}")
    print(f"Test: {test_config.name}, config: {test_config.config}")
    print()
