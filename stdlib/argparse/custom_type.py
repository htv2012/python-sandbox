#!/usr/bin/env python3
"""
custom_type.py
whatis: Custom type with argparse
"""

import argparse


class ConfigFile:
    """ A custom type """

    def __init__(self, filename=None):
        if filename is not None:
            self.filename = filename

    def __str__(self):
        return "ConfigFile: {}".format(self.filename)


def main():
    """ Entry """
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", type=ConfigFile)

    args = parser.parse_args(["-c", "foo"])
    assert isinstance(args.config, ConfigFile)
    print(args.config)


if __name__ == "__main__":
    main()
