#!/usr/bin/env python
from __future__ import print_function, unicode_literals

import argparse
import logging
import os

logging.basicConfig(level=os.getenv("LOGLEVEL", logging.WARN))
logger = logging.getLogger(__name__)


def find_uppath(filename, path):
    """Find a file in the path, if not found, keep going up parent dir"""
    target = os.path.normpath(os.path.join(path, filename))
    if os.path.exists(target):
        return target

    path = os.path.normpath(path)
    parent = os.path.dirname(path)

    if path == parent:
        return ""

    return find_uppath(filename, parent)


def tryout(target, path):
    found = find_uppath(target, path)
    logger.debug("Path: {}".format(path))
    logger.debug("File: {}".format(target))
    print(found)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", default=os.getcwd())
    parser.add_argument("filename")
    arguments = parser.parse_args()

    tryout(arguments.filename, arguments.dir)
