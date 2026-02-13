#!/usr/bin/env python3
import enum
import json
import pathlib

import click


def create_config() -> enum.Enum:
    config_dir = pathlib.Path(__file__).with_name("config")
    assert config_dir.exists()
    name_value = {path.stem.upper(): path for path in config_dir.glob("*")}
    return enum.Enum("Config", name_value)


Config = create_config()


@click.command
@click.argument("config", type=click.Choice(Config, case_sensitive=False))  # type: ignore
def main(config):
    with open(config.value) as stream:
        data = json.load(stream)

    for key, value in data.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
