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


class ConfigParam(click.Choice):
    def __init__(self):
        root = (
            pathlib.Path(__file__).with_name("config").relative_to(pathlib.Path.cwd())
        )
        self.path = {path.stem: path for path in root.glob("*.yaml")}

        with contextlib.suppress(KeyError):
            aliases_file = self.path.pop("_aliases")
            with open(aliases_file, "rb") as stream:
                self.aliases = yaml.safe_load(stream)
            for alias, name in self.aliases.items():
                self.path[alias] = self.path[name]

        super().__init__(self.path, case_sensitive=False)

    def convert(self, value, param, ctx):
        value = super().convert(value, param, ctx)
        return ConfigFile(value, self.path[value])


@click.command
@click.option("-c", "--config", type=ConfigParam(), required=True)
def main(config):
    print(f"{config = }")
    print(f"{config.content = }")
