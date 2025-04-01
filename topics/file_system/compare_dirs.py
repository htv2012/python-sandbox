#!/usr/bin/env python
"""Compare 2 directories"""

import os
import sys


def scan_dir(dir):
    fullpaths = set()
    for path, dirnames, filenames in os.walk(dir):
        # Remove the top dir from path, which helps with comparison
        # If path              = foo/bar/one/two/three.c then
        #    path_without_root =     bar/one/two/three.c
        path_without_root = path.split(os.sep, 1)[1]

        for filename in filenames:
            fullpath = os.path.join(path_without_root, filename)
            fullpaths.add(fullpath)
    return fullpaths


def show_difference(dir, diff_set):
    print("\nFiles that are only in {0}:".format(dir))
    for filename in sorted(diff_set):
        print(filename)


def main():
    dir1 = sys.argv[1]
    dir2 = sys.argv[2]
    db1 = scan_dir(dir1)
    db2 = scan_dir(dir2)

    show_difference(dir1, db1 - db2)
    show_difference(dir2, db2 - db1)


if __name__ == "__main__":
    main()
