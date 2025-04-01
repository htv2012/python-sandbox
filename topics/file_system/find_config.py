#!/usr/bin/env python
"""
whatis: find configuration file from various places
"""

import itertools
import os


def find_config_files(base_names, locations):
    """
    Given a list of base names and a list of locations, return a list of path
    names which exist.
    """
    pathnames = []

    for path, name in itertools.product(locations, base_names):
        pathname = os.path.join(path, name)
        if os.path.exists(pathname) and pathname not in pathnames:
            pathnames.append(pathname)

    return pathnames


if __name__ == "__main__":
    filenames = ["nav.ini", ".nav.ini", "nav.txt", ".nav.txt"]
    dirs = [
        os.path.expanduser("~"),
        "C:\\Users\hvu",
        "D:\\CloudStation\\src\\workspaces",
        os.path.expanduser("~/src/workspaces"),
    ]
    print("\n".join(find_config_files(filenames, dirs)))
