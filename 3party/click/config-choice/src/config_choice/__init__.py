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
        self.config = {path.stem: path for path in root.glob("*.yaml")}
        try:
            aliases_file = self.config.pop("_aliases")
            with open(aliases_file, "rb") as stream:
                self.aliases = yaml.safe_load(stream)
            for alias, name in self.aliases.items():
                self.config[alias] = self.config[name]
        except KeyError:
            pass

        super().__init__(self.config, case_sensitive=False)

    def convert(self, value, param, ctx):
        if value not in self.choices:
            self.fail(f" {value} is not one of {', '.join(self.choices)}")
        return ConfigFile(value, self.config[value])


@click.command
@click.option("-c", "--config", type=ConfigParam(), required=True)
def main(config):
    print(f"{config = }")
    print(f"{config.content = }")
