import enum
import functools
import pathlib

import click
import yaml

CONFDIR = pathlib.Path(__file__).with_name("venue_config")


class Conf(enum.Enum):
    DevPit1 = "devpit_1"
    DevPit2 = "devpit_2"
    DevPit = "devpit"
    TreasureIsland = "treasure_island"

    @functools.cached_property
    def path(self):
        value = self.value
        if value == "devpit" or value == "treasure_island":
            value = "devpit_1"
        return CONFDIR / f"{value}.yaml"

    @functools.cached_property
    def content(self):
        with open(self.path, "rb") as stream:
            return yaml.safe_load(stream)

    @classmethod
    def names(cls):
        return [v.name for v in cls]


@click.command
@click.option(
    "-v",
    "--venue",
    type=click.Choice(Conf.names(), case_sensitive=False),
    required=True,
)
def main(venue) -> None:
    print(f"{venue = }")
    venue = Conf[venue]

    print(f"{venue = }")
    print(f"{venue.content = }")


if __name__ == "__main__":
    main()
