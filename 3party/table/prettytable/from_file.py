#!/usr/bin/env python3
import pathlib

import prettytable


def from_file(path: pathlib.Path):
    print(f"\n# {path}")
    file_type = path.suffix
    if file_type == ".json":
        with open(path) as stream:
            return prettytable.from_json(stream.read())
    elif file_type == ".csv":
        with open(path) as stream:
            return prettytable.from_csv(stream)


def show(path: pathlib.Path):
    table = from_file(path)
    print(table)


data_dir = pathlib.Path("data")
for path in data_dir.glob("*"):
    show(path)
