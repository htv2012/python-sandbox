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

terms = " or ".join("body like ?" for term in options.terms)
sql = f"select title from notes where {terms}"
logging.debug("sql=%r", sql)
logging.debug("terms=%r", options.terms)

with db.connect() as connection:
    for (title,) in connection.execute(
        f"select title from notes where {terms}",
        [f"%{term}%" for term in options.terms],
    ):
        print(title)
