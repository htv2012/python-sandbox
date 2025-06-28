import enum
import functools
import pathlib

import click
import yaml

CONFDIR = (
    pathlib.Path(__file__).with_name("venue_config").relative_to(pathlib.Path.cwd())
)
CONF_ALIASES = {
    "devpit": "devpit_1",  # devpit is an alias for devpit_1
    "treasure_island": "devpit_1",  # treasure_island is an alias for devpit_1
}


class ConfigFile(enum.Enum):
    """A configuration file."""

    DevPit1 = "devpit_1"
    DevPit2 = "devpit_2"
    DevPit = "devpit"
    TreasureIsland = "treasure_island"
    FS1 = "flatsat_1"

    @functools.cached_property
    def path(self):
        """Path to the configuration file."""
        base_name = CONF_ALIASES.get(self.value, self.value)
        return CONFDIR / f"{base_name}.yaml"

    @functools.cached_property
    def content(self):
        """Content of the configuration file."""
        with open(self.path, "rb") as stream:
            return yaml.safe_load(stream)

    @classmethod
    def names(cls):
        """Names of the members."""
        return [v.name for v in cls]

    @classmethod
    def from_param(cls, ctx, param, value):
        """Callback to convert string value to member."""
        return cls[value]

    @property
    def is_devpit(self):
        """Return True if member is a dev pit, else return False."""
        return "devpit" in self.name.casefold()


@click.command
@click.option(
    "-v",
    "--venue",
    type=click.Choice(ConfigFile.names(), case_sensitive=False),
    callback=ConfigFile.from_param,
    required=True,
)
def main(venue) -> None:
    print()
    print(f"Name: {venue}")
    print(f"Value: {venue.value}")
    print(f"Path: {venue.path}")
    print(f"Content: {venue.content}")
    print(f"Is it a dev pit? {venue.is_devpit}")
    print()


if __name__ == "__main__":
    main()
