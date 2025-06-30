import click

from .config.venue_config import ConfigFile, ConfigFileType


@click.command
@click.option("--venue", type=ConfigFileType(), required=True)
def main(venue: ConfigFile):
    print(f"Venue ID: {venue.venue_id}")
    print(f"Path: {venue.path}")
    print(f"Config: {venue.config}")
    print(f"Is it a dev pit? {venue.is_devpit}")
    print()
