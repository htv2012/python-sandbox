"""
Search Notes
"""
import argparse
import db

parser = argparse.ArgumentParser()
parser.add_argument("terms", nargs="+")
options = parser.parse_args()
print(options)

terms = " or ".join("term like %?%" for term in options.terms)
print(terms)

with db.connect() as connection:
    for (title,) in connection.execute(f"select title from notes where {terms}", options.terms):
        print(title)