#!/usr/bin/env python3
import enum
import json
import pathlib

config_dir = pathlib.Path(__file__).with_name("config")
assert config_dir.exists()


class Config(enum.Enum):
    TESTBED = ("testbed", "testbed.json")
    STAGING = ("staging", "staging.json")
    PRODUCTION = ("production", "production.json")

    def __init__(self, value: int, path: str):
        self._value_ = value
        self.path = config_dir / path

    @property
    def cfg(self):
        with open(self.path) as stream:
            config = json.load(stream)
        return config


def main():
    config = Config.TESTBED
    print(config)
    print(config.path)
    print(config.cfg)


if __name__ == "__main__":
    main()
