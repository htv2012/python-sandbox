#!/usr/bin/env python3
"""
Given a directory, find the name of the python package
"""

import pathlib 
import argparse


marker = '__init__.py'


def find_package(path_to_leaf):
    path = pathlib.Path(path_to_leaf).resolve()
    components = []

    while (path / marker).exists():
        components.insert(0, path.name)
        path = path.parent

    return '.'.join(components)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    options = parser.parse_args()
    print(find_package(options.path))

    path = pathlib.Path(options.path)

