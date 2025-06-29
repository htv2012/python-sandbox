import click

from .config.venue_config import ConfigFile, ConfigFileType


@click.command
@click.option("--venue", type=ConfigFileType(), required=True)
def main(venue: ConfigFile):
    print(f"{venue = }")
    print(f"{venue.config = }")
    print()
