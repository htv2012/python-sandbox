#!/usr/bin/env python3
"""
whatis: demo reading rows as custom namespace

This is an attempt to solve the problem with types.SimpleNamespace:
it reorder the columns alphabetically, thus changes the column order
in a CSV file.
"""
import csv
import pathlib


class Namespace:
    def __init__(self, **kwargs):
        self._columns = list(kwargs)
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __repr__(self):
        attributes = ", ".join(
            f"{name}={getattr(self, name)!r}" for name in self._columns
        )
        class_name = self.__class__.__name__
        return f"{class_name}({attributes})"

    @classmethod
    def from_dict(cls, dict_object):
        return cls(**dict_object)


def main():
    """Entry"""
    data_filename = pathlib.Path(__file__).with_name("users.csv")
    with open(data_filename, "r", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        for row in map(Namespace.from_dict, reader):
            print(row)


if __name__ == "__main__":
    main()
