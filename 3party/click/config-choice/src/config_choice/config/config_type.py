import contextlib
import dataclasses
import functools
import pathlib
from typing import Dict

import click
import yaml


@dataclasses.dataclass(frozen=True)
class Config:
    name: str
    path: pathlib.Path

    @functools.cached_property
    def config(self) -> Dict:
        """Return the venue_config value of the config file."""
        with open(self.path, "rb") as stream:
            return yaml.safe_load(stream)


class ConfigFile(Config):
    @functools.cached_property
    def config(self) -> Dict:
        ret = super().config
        return ret["venue_config"]


class ConfigType(click.Choice):
    """
    A click custom type to gather all configuration files as choices.

    If a configuration file is devpit1.yaml, then the choice for that
    file is "devpit1".

    Among the configuration files, there is an optional _aliases.yaml
    file, which specifies all the aliases. For example, treasureisland is
    an alias for devpit1. That means treasureisland will use devpit1.yaml
    as its configuration file.

    See: https://click.palletsprojects.com/en/stable/parameter-types/#how-to-implement-custom-types
    """

    name = "ConfigType"

    def __init__(self, root: pathlib.Path, cls=None):
        self.cls = cls or Config
        self.path: Dict[str, pathlib.Path] = {
            path.stem: path for path in root.glob("*.yaml")
        }

        with contextlib.suppress(KeyError):
            # File _aliases.yaml is optional. That means
            # the following line might raise a KeyError
            aliases_file = self.path.pop("_aliases")

            # _aliases.yaml file exists, add them to the
            # choices
            with open(aliases_file, "rb") as stream:
                aliases = yaml.safe_load(stream)
            for alias, name in aliases.items():
                self.path[alias] = self.path[name]

        super().__init__(sorted(self.path), case_sensitive=False)

    def convert(self, value, param, ctx):
        # Call the base class' convert() to ensure the
        # argument from command-line is a valid choice
        value: str = super().convert(value, param, ctx)

        # Convert from a string argument to ConfigFile
        return self.cls(value, self.path[value])
