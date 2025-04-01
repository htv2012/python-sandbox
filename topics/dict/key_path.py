#!/usr/bin/env python3
"""
Given a nested JSON object and a list of keys, navigate the object and
get the value
"""

import json
from typing import Union


def get_value(dict_object, key_path, separator="."):
    if isinstance(key_path, str):
        key_path = key_path.split(separator)
    value = dict_object

    for key in key_path:
        if isinstance(value, list):
            try:
                key = int(key)
            except ValueError:
                raise ValueError("Invalid key: {}".format(key))
        value = value[key]
    return value


def try_path(json_object: dict, key_path: Union[tuple, str]):
    result = get_value(json_object, key_path)
    print(f"\n# {key_path=}\n{result}")


def main():
    """entry"""
    json_object = {
        "name": "John Doe",
        "phones": {"home": "555-1212", "mobile": "555-2222"},
        "emails": {
            "personal": ["abc@example.com", "def@example.com"],
            "work": "foo@bar.com",
        },
    }

    print("\n# JSON Object")
    print(json.dumps(json_object, indent=4))
    try_path(json_object, "name")
    try_path(json_object, ("phones", "mobile"))
    try_path(json_object, "emails.personal.1")
    try_path(json_object, "emails.work")


if __name__ == "__main__":
    main()
