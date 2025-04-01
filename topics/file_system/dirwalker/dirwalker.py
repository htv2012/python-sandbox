#!/usr/bin/env python

import os
from fnmatch import fnmatch


def exclude(*patterns):
    """A predicate which excludes any file that matches a pattern"""

    def predicate(filename):
        return not any(fnmatch(filename, pattern) for pattern in patterns)

    return predicate


def include(*patterns):
    """A predicate which includes only files that match a list of patterns"""

    def predicate(filename):
        return any(fnmatch(filename, pattern) for pattern in patterns)

    return predicate


def dirwalker(root, predicate=None):
    """Recursively walk a directory and yield the path names"""
    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            fullpath = os.path.join(dirpath, filename)
            if predicate is None or predicate(filename):
                yield fullpath
