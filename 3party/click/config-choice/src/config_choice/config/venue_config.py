import contextlib
import dataclasses
import functools
from pathlib import Path
from typing import Dict

import click
import yaml


@dataclasses.dataclass(frozen=True)
class ConfigFile:
    """
    Represent a venue configuration file, which consists of the following attributes

    venue_id: Identify a venue, e.g. "devpit1"
    path: the path to the configuration file
    config: The venue_config value of the file, a dictionary
    """

    venue_id: str
    path: Path

    @functools.cached_property
    def config(self) -> Dict:
        """Return the venue_config value of the config file."""
        with open(self.path, "rb") as stream:
            return yaml.safe_load(stream)["venue_config"]

    @property
    def is_devpit(self):
        return self.venue_id.startswith("devpit") or self.venue_id == "treasureisland"


class ConfigFileType(click.Choice):
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

    def __init__(self):
        root = Path(__file__).with_name("venue_config")
        self.path: Dict[str, Path] = {path.stem: path for path in root.glob("*.yaml")}

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

    def convert(self, value, param, ctx) -> ConfigFile:
        # Call the base class' convert() to ensure the
        # argument from command-line is a valid choice
        value: str = super().convert(value, param, ctx)

        # Convert from a string argument to ConfigFile
        return ConfigFile(value, self.path[value])
