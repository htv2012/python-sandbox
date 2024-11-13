#!/usr/bin/env python3
"""Transform each row into a named tuple."""
import csv
import collections
import pathlib


def dict_to_namedtuple(dict_object):
    """Convert a dictionary to a named tuple."""
    User = collections.namedtuple("User", dict_object)
    transformed_object = User(**dict_object)
    return transformed_object


def main():
    """Entry"""
    data_path = pathlib.Path(__file__).with_name("users.csv")
    with open(data_path, "r", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        for row in map(dict_to_namedtuple, reader):
            print(row)


if __name__ == "__main__":
    main()
