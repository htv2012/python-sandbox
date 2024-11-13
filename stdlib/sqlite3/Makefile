.PHONY: help, interact, custom, clean

custom: temp-db.sqlite
	python3 custom_rows.py

interact: temp-db.sqlite
	sqlite3 temp-db.sqlite

clean:
	rm -f temp-db.sqlite

temp-db.sqlite: create_database.sql
	sqlite3 temp-db.sqlite < create_database.sql

