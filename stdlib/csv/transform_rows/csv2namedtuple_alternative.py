#!/usr/bin/env python3
"""Transform each row into a named tuple."""
import csv
import pathlib
import typing


class User(typing.NamedTuple):
    uid: int
    alias: str
    shell: str

    @classmethod
    def from_tuple(cls, tuple_object):
        return cls(*tuple_object)


def main():
    """Entry"""
    data_path = pathlib.Path(__file__).with_name("users.csv")
    with open(data_path, "r", encoding="utf-8") as stream:
        reader = csv.reader(stream)
        next(reader)
        for row in map(User.from_tuple, reader):
            print(row)


if __name__ == "__main__":
    main()
