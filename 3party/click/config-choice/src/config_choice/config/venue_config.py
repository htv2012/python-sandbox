import contextlib
import dataclasses
import functools
import pathlib

import click
import yaml


@dataclasses.dataclass(frozen=True)
class ConfigFile:
    """
    Represent a venue configuration file, which consists of the following attributes

    venue_id: Identify a venue, e.g. "devpit1"
    path: the path to the configuration file
    content: The parsed content of the file, a dictionary
    """

    venue_id: str
    path: pathlib.Path

    @functools.cached_property
    def content(self):
        with open(self.path, "rb") as stream:
            return yaml.safe_load(stream)["venue_config"]


class ConfigType(click.Choice):
    """
    A click custom type to gather all configuration files as choices.

    If a configuration file is devpit1.yaml, then the choice for that
    file is "devpit1".
    
    Among the configuration files, there is a special _aliases.yaml file,
    which specifies all the aliases. For example, treasureisland is an
    alias for devpit1. That means treasureisland will use devpit1.yaml
    as its configuration file.

    The click return type will be ConfigFile.
    """
    def __init__(self):
        root = (
            pathlib.Path(__file__)
            .with_name("venue_config")
            .relative_to(pathlib.Path.cwd())
        )
        self.path = {path.stem: path for path in root.glob("*.yaml")}

        # If there is an _aliases.yaml, process it
        with contextlib.suppress(KeyError):
            aliases_file = self.path.pop("_aliases")
            with open(aliases_file, "rb") as stream:
                aliases = yaml.safe_load(stream)
            for alias, name in aliases.items():
                self.path[alias] = self.path[name]

        super().__init__(self.path, case_sensitive=False)

    def convert(self, value, param, ctx):
        # Call the base class' convert() to ensure the
        # argument from command-line is valid
        value = super().convert(value, param, ctx)

        # Convert from a string to ConfigFile
        return ConfigFile(value, self.path[value])
