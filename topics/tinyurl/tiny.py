#!/usr/bin/env python
import argparse
import logging
import os
import pathlib
import random
import sqlite3
import string
import webbrowser

logging.basicConfig(level=os.getenv("LOGLEVEL", logging.WARN))
logger = logging.getLogger(__name__)


def get_config():
    return {"dbfile": __file__.replace(".py", ".sqlite")}


def generate_token():
    population = (string.ascii_letters + string.digits) * 6
    token = "".join(random.sample(population, 6))
    return token


def add(db, url, token=None):
    # Detect existing URL
    sql = "SELECT count(url) FROM tiny WHERE url = ?"
    (url_count,) = db.execute(sql, (url,)).fetchone()
    if url_count != 0:
        print(f"URL {url} is already added")
        return

    while token is None:
        token = generate_token()
        cursor = db.execute("select token from tiny where token=?", (token,))
        if cursor.fetchone() is None:
            break
        else:
            token = None

    db.execute("insert into tiny values (?, ?)", (token, url))
    print(f"{token}: {url}")


def list_all(db):
    for token, url in db.execute("select token, url from tiny"):
        print(f"{token}: {url}")


def search(db, search_term):
    search_term = f"%{search_term}%"
    sql = "SELECT token, url FROM tiny WHERE token LIKE ? OR url LIKE ? ORDER BY token"
    for token, url in db.execute(sql, (search_term, search_term)):
        print(f"{token}: {url}")


def open_by_token(db, token):
    sql = "SELECT url FROM tiny WHERE token = ?"
    for (url,) in db.execute(sql, (token,)):
        webbrowser.open(url)


def parse_command_line():
    parser = argparse.ArgumentParser()
    action = parser.add_subparsers(dest="action")
    action.required = True

    add_sub_command = action.add_parser("add")
    add_sub_command.add_argument("-t", "--token")
    add_sub_command.add_argument("url")

    find_sub_command = action.add_parser("find")
    find_sub_command.add_argument("term")

    action.add_parser("open").add_argument("token")

    action.add_parser("ls")

    options = parser.parse_args()
    return options


def main():
    dbfile = pathlib.Path(__file__).with_suffix(".sqlite")
    options = parse_command_line()

    with sqlite3.connect(dbfile) as db:
        if options.action == "add":
            add(db, options.url, options.token)
        elif options.action == "find":
            search(db, options.term)
        elif options.action == "ls":
            list_all(db)
        elif options.action == "open":
            open_by_token(db, options.token)


if __name__ == "__main__":
    main()
