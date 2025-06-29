import contextlib
import dataclasses
import functools
import pathlib

import click
import yaml


@dataclasses.dataclass(frozen=True)
class ConfigFile:
    value: str
    path: pathlib.Path

    @functools.cached_property
    def content(self):
        with open(self.path, "rb") as stream:
            return yaml.safe_load(stream)


class ConfigType(click.Choice):
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
        value = super().convert(value, param, ctx)
        return ConfigFile(value, self.path[value])
