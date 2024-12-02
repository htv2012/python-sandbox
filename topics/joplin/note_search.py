#!/usr/bin/env python3
"""
Search Notes
"""

import argparse
import os

import db


parser = argparse.ArgumentParser()
parser.add_argument("terms", nargs="+")
options = parser.parse_args()

with db.connect() as connection:
    for (title,) in db.search(connection, options.terms, columns_csv='title'):
        print(title)
