#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Using a sqlite database to implement a table
"""


import csv
import os
import sqlite3


class Table(object):
    def _create_db(self, headers):
            try:
                os.unlink('table.sqlite3')
            except OSError:
                pass
            self.db = sqlite3.connect('table.sqlite3')
            # self.db = sqlite3.connect(':memory:')
            cursor = self.db.cursor()
            columns = ['{} TEXT'.format(c) for c in headers]
            sql = 'CREATE TABLE mytable ({})'.format(', '.join(columns))
            cursor.execute(sql)
            self.db.commit()

    def __init__(self, headers, rows):
        self._headers = headers[:]
        self._create_db(headers)
        cursor = self.db.cursor()
        place_holders = ','.join(['?'] * len(headers))
        sql = 'INSERT INTO mytable VALUES ({})'.format(place_holders)
        cursor.executemany(sql, rows)
        self.db.commit()

    @classmethod
    def from_csv(cls, csv_file):
        with open(csv_file) as f:
            reader = csv.reader(f)
            headers = next(reader)
            return cls(headers, reader)

    @property
    def rows_count(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT COUNT(*) FROM mytable')
        rows_count, = cursor.fetchone()
        return rows_count

    @property
    def columns_count(self):
        return len(self._headers)

    @property
    def headers(self):
        return self._headers[:]

    def __iter__(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM mytable')
        while True:
            row = cursor.fetchone()
            if row is None:
                break
            yield row


if __name__ == '__main__':
    table = Table.from_csv('table_example.csv')
    print('Rows:', table.rows_count)
    print('Columns:', table.columns_count)
    print('Headers:', table.headers)

    for row in table:
        print(row)
