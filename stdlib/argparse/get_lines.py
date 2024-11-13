#!/usr/bin/env python
"""
Given a file name a a list of lines, displays the lines
For example:

    filename 3-4 18 37 50-53

"""
import argparse
from itertools import chain
import linecache


def base_1_range(value):
    try:
        return [int(value)]
    except ValueError:
        try:
            start, stop = value.split("-")
            start = int(start)
            stop = int(stop)
            return range(start, stop + 1)
        except:
            raise argparse.ArgumentTypeError(f"Invalid index: {value}")


def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("lines", nargs="*", type=base_1_range)
    options = parser.parse_args()
    options.lines = set(chain.from_iterable(options.lines))

    return options


if __name__ == "__main__":
    options = get_options()
    for line_number in sorted(options.lines):
        line = linecache.getline(options.filename, line_number)
        print(f"{line_number:>4} {line}", end="")
