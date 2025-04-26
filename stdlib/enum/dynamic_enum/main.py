#!/usr/bin/env python3
import enum
import pathlib


def create_config() -> enum.Enum:
    config_dir = pathlib.Path(__file__).with_name("config")
    assert config_dir.exists()
    name_value = {path.stem.upper(): path for path in config_dir.glob("*")}
    return enum.Enum("Config", name_value)


Config = create_config()


def main():
    for c in Config:
        print(c)


if __name__ == "__main__":
    main()
