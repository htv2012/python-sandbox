#!/usr/bin/env python3
import enum
import json
import pathlib

import click


def create_config() -> enum.Enum:
    config_dir = pathlib.Path(__file__).with_name("config")
    assert config_dir.exists()
    pair = []
    for path in config_dir.glob("*.json"):
        with open(path) as stream:
            key = path.stem.upper()
            value = json.load(stream)
            pair.append((key, value))
    return enum.Enum("Config", pair)


Config = create_config()


@click.command
@click.argument("config", type=click.Choice(Config, case_sensitive=False))  # type: ignore
def main(config):
    for key, value in config.value.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
