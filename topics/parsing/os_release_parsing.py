#!/usr/bin/env python3
"""
Uses csv to parse /etc/os-release
"""

import csv
import pathlib
from pprint import pprint


def main():
    """Entry"""
    path = pathlib.Path("/etc/os-release")
    if not path.exists():
        raise SystemExit("/etc/os-release does not exist, cannot parse")

    with open(path) as stream:
        reader = csv.reader(stream, delimiter="=")
        os_release = dict(reader)
        pprint(os_release)


if __name__ == "__main__":
    main()
