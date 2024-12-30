#!/usr/bin/env python
import json
import pathlib

import fire


CONFIG_PATH = pathlib.Path("/tmp/example2_class.json")


def get_settings():
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as stream:
            settings = json.load(stream)
            return settings
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        return {}


class MyStuff:
    def get(self, key):
        """
        Reads the key and returns its value

        :param key: The key to search
        :return: The value
        """
        settings = get_settings()
        print(f"{key} = {settings.get(key)}")

    def set(self, key, value):
        """
        Set the key/value pair

        :param key: The name of the key
        :param value: The value of the key
        """
        settings = get_settings()
        settings[key] = value
        with open(CONFIG_PATH, "w", encoding="utf-8") as stream:
            json.dump(settings, stream, indent=4)


if __name__ == '__main__':
    fire.Fire(MyStuff)
