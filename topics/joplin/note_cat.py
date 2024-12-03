#!/usr/bin/env python3
"""
Search Notes
"""

import argparse
import os

import db


parser = argparse.ArgumentParser()
parser.add_argument("title")
options = parser.parse_args()

with db.connect() as connection:
    for row in db.search_by_title(connection, options.title):
