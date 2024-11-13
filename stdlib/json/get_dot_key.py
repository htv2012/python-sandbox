#!/usr/bin/env python
"""Generate dotted keys from a nested dictionary."""

from typing import Union

SEPARATOR = "."


def get_dot_key(json_object: Union[list, dict], path: str, default=None):
    """
    Take a JSON object and a path and return the value. If not
    found, return the value specified by the default parameter.

    :param json_object: The JSON object
    :param path: A path to a value in the dictionary
    :param default: The default value when not found
    :return: The value specified by the path

    >>> get_dot_key({'a': {'b': {'c': 5}}}, 'a.b.c')
    5
    """
    current = json_object
    keys = path.strip(SEPARATOR).split(SEPARATOR)

    try:
        for k in keys:
            if isinstance(current, list):
                k = int(k)
            current = current[k]
        return current
    except (KeyError, TypeError, IndexError):
        return default


if __name__ == "__main__":
    json_data = [
        {
            "name": {"first": "John", "last": "Wayne"},
            "phone": {"mobile": "555-1212", "work": "567-8901"},
        },
        {
            "name": {"first": "Jane", "last": "Fonda"},
            "phone": {"mobile": "555-1234", "work": "567-1234"},
        },
    ]

    print("0.name.first.:", get_dot_key(json_data, "0.name.first."))
    print("1.name.first.:", get_dot_key(json_data, "1.name.first."))
