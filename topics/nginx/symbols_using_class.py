#!/usr/bin/env python3
"""Load symbols as a class, access as dict or object."""
import argparse
import collections.abc
import json
import os


class Symbols(collections.abc.Mapping):
    def __init__(self, path=None):
        path = path or os.getenv("TESTRUN_SYMBOLS") or os.getenv("SYSTEST_SYMBOLS")
        with open(path) as stream:
            self._data = json.load(stream)
        for k, v in self._data.items():
            setattr(self, k, v)

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __getitem__(self, name):
        return self._data[name]


def main():
    """Entry"""
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?")
    options = parser.parse_args()

    symbols = Symbols(options.path)

    # Access the keys/values, as in a dict
    for key, value in symbols.items():
        print(f"{key}={value!r}")

    print("\n# Access the attributes, as in an object")
    print(f"ctrl_admin_email: {symbols.ctrl_admin_email}")
    print(f"ctrl_admin_pass: {symbols.ctrl_admin_pass}")

    print("\n# Access the keys, as in a dict")
    print(f"ctrl_dashboard_url: {symbols['ctrl_dashboard_url']}")
    print(f"ctrl_os: {symbols['ctrl_os']}")


if __name__ == "__main__":
    main()
