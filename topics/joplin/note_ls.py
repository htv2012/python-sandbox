"""
List Notes Titles
"""
import db

with db.connect() as connection:
    for (title,) in connection.execute("select title from notes"):
        print(title)