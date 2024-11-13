#!/usr/bin/env python
import argparse
import json
import random
import sqlite3
import string
import logging
import os


logging.basicConfig(level=os.getenv('LOGLEVEL', logging.WARN))
logger = logging.getLogger(__name__)


def get_config():
    return {'dbfile': __file__.replace('.py', '.sqlite')}


def generate_token():
    population = (string.ascii_letters + string.digits) * 6
    token = ''.join(random.sample(population, 6))
    return token


class Tiny:
    def __init__(self, database_filename):
        self.dbfile = database_filename

    def add(self, url):
        row = find_by_url(url)
        if row['status'] == 'OK':
            row['status'] = 'url already exists'
            return row

        with sqlite3.connect(self.dbfile) as db:
            while True:
                token = generate_token()
                logger.debug('new token generated: %r', token)
                cursor = db.execute("select token from tiny where token=?",
                                    (token,))
                logger.debug('cursor: %r', cursor)
                if cursor.fetchone() is None:
                    break

            db.execute("insert or ignore into tiny values (?, ?)", (token, url))
            cursor = db.execute("select token, url from tiny where url=?", (url,))
            row = cursor.fetchone()

            result = dict(token=row[0], url=row[1], status='OK')
            return result


    def find_by_token(self, token):
        with sqlite3.connect(self.dbfile) as db:
            cursor = db.execute(
                    "select token, url from tiny where token=?",
                    (token,))
            row = cursor.fetchone()

            if row is None:
                result = dict(token=token, url='', status='not found')
            else:
                result = dict(token=row[0], url=row[1], status='OK')

            return result


    def find_by_url(self, url):
        with sqlite3.connect(self.dbfile) as db:
            cursor = db.execute("select token, url from tiny where url=?", (url,))
            row = cursor.fetchone()
            if row:
                return dict(token=row[0], url=row[1], status='OK')
            else:
                return dict(token='', url=url, status='not found')


    def list_all(self):
        with sqlite3.connect(self.dbfile) as db:
            cursor = db.execute('select token, url from tiny')
            rows = [dict(token=row[0], url=row[1]) for row in cursor]
            return dict(entries=rows, status='OK')


config = get_config()
tiny = Tiny(config['dbfile'])

add = tiny.add
find_by_token = tiny.find_by_token
find_by_url = tiny.find_by_url
list_all = tiny.list_all


def main():
    parser = argparse.ArgumentParser()
    actions = parser.add_subparsers(dest='command')

    add_sub_command = actions.add_parser('add')
    add_sub_command.add_argument('-t', '--token')
    add_sub_command.add_argument('url')

    find_sub_command = actions.add_parser('find')
    find_sub_command.add_argument('token')

    actions.add_parser('list')

    args = parser.parse_args()

    if args.command == 'add':
        result = add(args.url)
    elif args.command == 'find':
        result = find_by_token(args.token)
    elif args.command == 'list':
        result = list_all()

    print((json.dumps(result, sort_keys=True, indent=4)))


if __name__ == '__main__':
    main()
