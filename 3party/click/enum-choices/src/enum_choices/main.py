import enum
import functools
import pathlib

import click
import yaml


class Star(enum.Enum):
    ELVIS = ("Elvis", "elvis.yaml")
    MARILYN = ("Marilyn", "marilyn.yaml")
    MONROE = ("Monroe", "marilyn.yaml")  # Same as Marilyn

    def __init__(self, value, path):
        self._value_ = value
        self.path = pathlib.Path(__file__).parent / "config" / path

    @functools.cached_property
    def config(self):
        with open(self.path, "rb") as stream:
            return yaml.safe_load(stream)


@click.command
@click.option(
    "--star", type=click.Choice(Star, case_sensitive=False), default=Star.ELVIS
)
def main(star):
    print(f"{star.name=}")
    print(f"{star.value=}")
    print(f"{star.path=}")
    print(f"{star.config=}")
