import sqlite3
import sys

con = sqlite3.connect('test.db')

with con:
    cur = con.cursor()
    cur.execute("SELECT * from Cars where Price >= 30000")

    rows = cur.fetchall()

    print('Cars that are $30K and up:\n')

    format_str = '{:>3} {:<15} {:>11,}'
    header_str = '{:>3} {:<15} {:>11}'
    print(header_str.format('Id', 'Name', 'Price (USD)'))
    for row in rows:
        print(format_str.format(*row))

