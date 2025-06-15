import enum
import functools
import pathlib

import click
import yaml


class Star(enum.Enum):
    ELVIS = ("Elvis", "elvis.yaml")
    MARILYN = ("Marilyn", "marilyn.yaml")
    MONROE = ("Monroe", "marilyn.yaml")  # Same config as Marilyn
    MARY_LOU = ("Mary-Lou", "mary-lou.yaml")

    def __init__(self, value, path):
        self._value_ = value
        self.path = pathlib.Path(__file__).parent / "config" / path
        self.path = self.path.relative_to(pathlib.Path.cwd())

    @functools.cached_property
    def config(self):
        with open(self.path, "rb") as stream:
            return yaml.safe_load(stream)

    @classmethod
    def to_names(cls):
        return [e.name.replace("_", "-") for e in cls]

    @classmethod
    def from_str(cls, name: str):
        name = name.replace("-", "_").upper()
        return cls[name]


@click.command
@click.option(
    "--star",
    type=click.Choice(Star.to_names(), case_sensitive=False),
    default="Elvis",
)
def main(star):
    star = Star.from_str(star)
    print(f"{star=}")
    print(f"{star.path=}")
    print(f"{star.config=}")
