#!/usr/bin/env python3
"""
Search Notes
"""

import argparse

import db

parser = argparse.ArgumentParser()
parser.add_argument("title")
options = parser.parse_args()


with db.connect() as connection:
    column_names = db._get_column_names(connection=connection, table_name="notes")
    for row_dict in db.search_by_title(connection, options.title):
        print(row_dict["body"])
