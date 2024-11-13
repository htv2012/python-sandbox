#!/usr/bin/env python
import logging
import sqlite3
import contextlib


class SQLiteHandler(logging.Handler):
    def __init__(self, filename, level=logging.NOTSET):
        super(SQLiteHandler, self).__init__(level)
        self._filename = filename
        self.connection = sqlite3.connect(filename)
        cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE `log` (
                    threadName TEXT,
                    name TEXT,
                    thread INTEGER,
                    created REAL,
                    process INTEGER,
                    processName TEXT,
                    args TEXT,
                    module TEXT,
                    levelname TEXT,
                    levelno INTEGER,
                    pathname TEXT,
                    lineno INTEGER,
                    msg TEXT,
                    funcName TEXT
                )
            """)
        # cursor.close()
        self.connection.commit()

    def emit(self, record):
        # cursor = self.connection.cursor()
        pass
