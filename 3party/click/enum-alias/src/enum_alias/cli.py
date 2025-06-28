import click

from .venue_config import ConfigFile


@click.command
@click.option(
    "-v",
    "--venue",
    type=click.Choice(ConfigFile.names(), case_sensitive=False),
    callback=ConfigFile.from_param,
    required=True,
)
def zerotouch(venue) -> None:
    print(f"Name: {venue}")
    print(f"Value: {venue.value}")
    print(f"Path: {venue.path}")
    print(f"Content: {venue.content}")
    print(f"Is it a dev pit? {venue.is_devpit}")
    print()


if __name__ == "__main__":
    zerotouch()
