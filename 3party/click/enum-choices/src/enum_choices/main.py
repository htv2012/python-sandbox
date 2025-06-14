import enum
import pathlib

import click
import yaml


class Car(enum.Enum):
    """ "Cars that are named after celebrities."""

    ELVIS = ("Elvis", "elvis.yaml")
    MARILYN = ("Marilyn", "marilyn.yaml")

    # Aliases
    MONROE = ("Monroe", "marilyn.yaml")

    def __init__(self, value, path):
        self._value_ = value
        self.path = path

    @property
    def config(self):
        path = pathlib.Path(__file__).parent / "config" / self.path
        with open(path, "rb") as stream:
            return yaml.safe_load(stream)


@click.command
@click.option(
    "-c", "--car", type=click.Choice(Car, case_sensitive=False), default=Car.ELVIS
)
def main(car):
    print(f"Nick Name: {car.name}")
    print(f"Name: {car.value}")
    print(f"Full Name: {car.config['Name']}")
    print(f"Configuration: {car.config}")
