"""
Database
"""

import pathlib
import sqlite3

from . import logger


def connect():
    root = pathlib.Path("~/.config/joplin-desktop").expanduser()
    db_path = root / "database.sqlite"
    logger.debug("db_path=%r", db_path)
    if not (db_path.exists() and not db_path.is_dir()):
        raise RuntimeError(f"Database does not exist: {db_path}")

    connection_uri = f"file:{db_path}?mode=ro"
    logger.debug("connection_uri=%r", connection_uri)

    return sqlite3.connect(connection_uri, uri=True)


def search(connection: sqlite3.Connection, terms: list[str], columns_csv="*"):
    sql = f"select {columns_csv} from notes where {' and '.join('body like ?' for _ in terms)}"
    logger.debug("sql=%r", sql)
    return connection.execute(sql, [f"%{term}%" for term in terms])


def search_by_title(connection: sqlite3.Connection, title: str):
    column_names = get_column_names(connection=connection, table_name="notes")
    for row in connection.execute(
        "select * from notes where title = ? collate nocase", (title,)
    ):
        yield dict(zip(column_names, row))


def get_column_names(connection: sqlite3.Connection, table_name: str) -> list:
    cursor = connection.execute(f"PRAGMA table_info({table_name})")
    column_names = [column[1] for column in cursor]
    return column_names
