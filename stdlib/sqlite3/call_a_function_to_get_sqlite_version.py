import sqlite3


if __name__ == '__main__':
    db = sqlite3.connect(':memory:')
    data = db.execute('SELECT SQLITE_VERSION()').fetchone()
    print('SQLite version: %s' % data)
