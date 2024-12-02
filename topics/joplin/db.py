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
    db_path = root / "database.sqlite"
    logging.debug("db_path=%r", db_path)
    if not (db_path.exists() and not db_path.is_dir()):
        raise RuntimeError(f"Database does not exist: {db_path}")

    return sqlite3.connect(f"file:{db_path}?mode=ro")


def search(connection: sqlite3.Connection, terms: list[str], columns_csv="*"):
    sql = f"select {columns_csv} from notes where {' and '.join('body like ?' for _ in terms)}"
    logging.debug("sql=%r", sql)
    return connection.execute(sql, [f"%{term}%" for term in terms])
