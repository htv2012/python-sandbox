#!/usr/bin/env python
"""
Uses namedtuple as a row
"""
import collections
import sqlite3


User = collections.namedtuple("User", ["uid", "alias", "shell"])
Group = collections.namedtuple("Group", ["gid", "name"])


def row_factory_func(cursor, row):
	# cursor.description = [
	#    ("uid", None, None, None, None, None, None),
	#    ...
	# ]
	# See: https://docs.python.org/3.6/library/sqlite3.html#sqlite3.Cursor.description

	if cursor.description[0][0] == "uid":
		return User._make(row)
	elif cursor.description[0][0] == "gid":
		return Group._make(row)


def main():
	users = [
		(501, "karen", "tcsh"),
		(502, "john", "bash"),
	]

	groups = [
		(1001, "admin"),
		(1002, "backup"),
	]

	connection = sqlite3.connect(":memory:")
	connection.execute("CREATE TABLE user (uid INT, alias TEXT, shell TEXT)")
	connection.executemany("INSERT INTO user VALUES (?, ?, ?)", users)
	connection.commit()
	connection.execute("CREATE TABLE grp (gid INT, name TEXT)")
	connection.executemany("INSERT INTO grp VALUES (?, ?)", groups)
	connection.commit()

	print("\nUser without setting row_factory")
	sql = "SELECT * FROM user"
	for row in connection.execute(sql):
		print(row)

	print("\nUser with setting row_factory")
	connection.row_factory = row_factory_func
	for row in connection.execute(sql):
		print(row)

	print("\nGroup with row_factory")
	for row in connection.execute("SELECT * FROM grp"):
		print(row)


if __name__ == '__main__':
	main()