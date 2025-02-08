#!/usr/bin/env python3
"""Import given a path"""

import argparse
import importlib.util
import pathlib


def import_path(path: pathlib.Path):
    """Given a path to a module, import and return that module"""
    path = pathlib.Path(path)
    name = path.stem

    spec = importlib.util.spec_from_file_location(name=name, location=path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=pathlib.Path)
    options = parser.parse_args()

    mod = import_path(options.path)
    mod.main()


if __name__ == "__main__":
    main()
