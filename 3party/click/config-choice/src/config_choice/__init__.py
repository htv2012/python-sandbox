import click

from .config.venue_config import ConfigType


@click.command
@click.option("--venue", type=ConfigType(), required=True)
def main(venue):
    print(f"{venue = }")
    print(f"{venue.content = }")
    print()
