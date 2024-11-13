#!/usr/bin/env python3
import collections
import pathlib
import sqlite3


def main():
    """Entry"""
    database_path = pathlib.Path(__file__).with_name("temp-db.sqlite")
    connection = sqlite3.connect(database_path)

    print()
    print("Users")
    User = collections.namedtuple("User", "uid,gid,alias,shell")
    connection.row_factory = lambda _, row: User._make(row)
    for row in connection.execute("SELECT * from users"):
        print(row)

    print()
    print("Groups")
    Group = collections.namedtuple("Group", "gid,name")
    connection.row_factory = lambda _, row: Group._make(row)
    for row in connection.execute("SELECT * FROM groups"):
        print(row)
    connection.row_factory = None


if __name__ == "__main__":
    main()
