"""
Database
"""

import logging
import os
import pathlib
import sqlite3

logging.basicConfig(
    level=os.getenv("LOGLEVEL", "WARNING"),
    format="%(levelname)-12s | %(message)s",
)


def connect():
    root = pathlib.Path("~/.config/joplin-desktop").expanduser()
    assert root.is_dir()

    db_path = root / "database.sqlite"
    logging.debug("db_path=%r", db_path)
    assert db_path.exists()
    assert not db_path.is_dir()

    return sqlite3.connect(f"file:{db_path}?mode=ro")


# c = connect()
# # query = "select id,title from notes"
# # for row in c.execute(query):
# #     print(row)

# # Search for text
# target = "mouse"
# target = f"%{target}%"
# for row in c.execute("select title from notes where body like ?", (target,)):
#     title = row[0]
#     # id_, title, body = row
#     # print("---")
#     print(title)
#     # print(body)