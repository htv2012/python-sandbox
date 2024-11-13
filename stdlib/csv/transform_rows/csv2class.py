#!/usr/bin/env python3
"""
whatis: convert row to custom class
"""
import csv
import dataclasses
import pathlib


@dataclasses.dataclass
class User:
    uid: int
    alias: str
    shell: str

    def __post_init__(self):
        self.uid = int(self.uid)

    @classmethod
    def from_tuple(cls, tuple_object):
        return cls(*tuple_object)

    @classmethod
    def from_dict(cls, dict_object):
        return cls(**dict_object)


def make_user(row):
    """From a CSV row, make a User object."""
    if isinstance(row, dict):
        return User(**row)
    if isinstance(row, (list, tuple)):
        return User(*row)
    raise ValueError(f"Expect dict, tuple, or list, but got {row!r}")


def main():
    """Entry"""
    data_filename = pathlib.Path(__file__).with_name("users.csv")

    # Use with a normal reader
    print("--- with User.from_tuple")
    with open(data_filename, "r", encoding="utf-8") as stream:
        reader = csv.reader(stream)
        next(reader)  # Skip the header row
        for row in map(User.from_tuple, reader):
            print(row)

    # Use with a dict reader
    print("--- with User.from_dict")
    with open(data_filename, "r", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        for row in map(User.from_dict, reader):
            print(row)

    # # In case we have to access to the class (e.g. part of some external
    # # library) We can write a custom factory function such as make_user
    # to # convert a row into a class
    print("--- with custom factory function")
    with open(data_filename, "r", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        for row in map(make_user, reader):
            print(row)


if __name__ == "__main__":
    main()
