#!/usr/bin/env python3
"""
Uses namedtuple as a row
"""

import collections
import sqlite3

User = collections.namedtuple("User", ["uid", "alias", "shell"])
Group = collections.namedtuple("Group", ["gid", "name"])
ROWS_FACTORY = {type_._fields: type_._make for type_ in [User, Group]}


def row_factory_func(cursor, row):
    fields = tuple(t[0] for t in cursor.description)
    type_ = ROWS_FACTORY.get(fields, tuple)
    return type_(row)


def create_database(connection: sqlite3.Connection):
    users = [
        (501, "karen", "tcsh"),
        (502, "john", "bash"),
    ]

    groups = [
        (1001, "admin"),
        (1002, "backup"),
    ]

    services = [
        (901, "serviceA"),
        (902, "serviceB"),
    ]

    connection.execute("create table user (uid int, alias text, shell text)")
    connection.executemany("insert into user values (?, ?, ?)", users)

    connection.execute("create table grp (gid int, name text)")
    connection.executemany("insert into grp values (?, ?)", groups)

    connection.execute("create table service (sid int, name text)")
    connection.executemany("insert into service values (?, ?)", services)

    connection.commit()
    connection.row_factory = row_factory_func


def main():
    with sqlite3.connect(":memory:") as connection:
        create_database(connection)

        print("\n# Users")
        for row in connection.execute("select * from user"):
            print(row)

        print("\n# Groups")
        for row in connection.execute("select * from grp"):
            print(row)

        print("\n# Services")
        for row in connection.execute("select * from service"):
            print(row)


if __name__ == "__main__":
    main()
