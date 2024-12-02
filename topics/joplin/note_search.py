#!/usr/bin/env python3
"""
Search Notes
"""

import argparse
import logging
import os

import db

logging.basicConfig(
    level=os.getenv("LOGLEVEL", "WARNING"),
    format="%(levelname)-12s | %(message)s",
)


parser = argparse.ArgumentParser()
parser.add_argument("terms", nargs="+")
options = parser.parse_args()

with db.connect() as connection:
    for (title,) in db.search(connection, options.terms, columns_csv='title'):
        print(title)
