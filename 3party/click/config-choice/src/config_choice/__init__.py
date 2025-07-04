import pathlib

import click

from .config.config_type import ConfigFile, ConfigType

TEST_CONFIG_DIR = pathlib.Path(__file__).parent / "config" / "test_configs"
VENUE_CONFIG_DIR = pathlib.Path(__file__).parent / "config" / "venue_configs"


@click.command
@click.option(
    "--venue", type=ConfigType(cls=ConfigFile, root=VENUE_CONFIG_DIR), required=True
)
@click.option(
    "--test-config",
    type=ConfigType(root=TEST_CONFIG_DIR),
    default="nightly",
    required=False,
)
def main(venue, test_config):
    print(f"Venue ID: {venue.name}, config: {venue.config}")
    print(f"Test: {test_config.name}, config: {test_config.config}")
    print()
