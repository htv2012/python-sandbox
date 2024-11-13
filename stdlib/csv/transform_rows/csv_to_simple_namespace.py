#!/usr/bin/env python3
"""
whatis: demo reading rows as SimpleNamespace

Plus: Simple
Minus: columns sorted alphabetically, thus mess up the original order
"""
import csv
import pathlib
import types


def make_namespace(row):
    """
    Transform a row from a dictionary to a simple namespace with uid
    converted to integer.
    """
    row = types.SimpleNamespace(**row)
    row.uid = int(row.uid)
    return row


def main():
    """Entry"""
    data_filename = pathlib.Path(__file__).with_name("users.csv")
    with open(data_filename, "r", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        for row in map(make_namespace, reader):
            print(row)


if __name__ == "__main__":
    main()
