#!/usr/bin/env python3
"""
Pass name/value over command line, decode values using JSON
"""

import argparse
import contextlib
import json


def decode_json_key_value(key_value):
    name, _, value = key_value.partition("=")

    # Attempt to JSON decode
    with contextlib.suppress(json.decoder.JSONDecodeError):
        value = json.loads(value)

    # If there is no equal sign, define the name as True
    if value == "":
        value = True
    return name, value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--define",
        nargs="+",
        action="extend",
        type=decode_json_key_value,
        metavar="name=value",
        help="Define name=value, or just name (which value will be true)",
        default=[],
    )
    options = parser.parse_args()
    settings = dict(options.define)
    print("define = ", end="")
    print(json.dumps(settings, indent=4))


if __name__ == "__main__":
    main()
