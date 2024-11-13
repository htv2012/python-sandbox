from __future__ import print_function, unicode_literals
import sqlite3


if __name__ == '__main__':
    cars = (
            (1, 'Audi', 52642),
            (2, 'Mercedes', 57127),
            (3, 'Soka', 9000),
            (4, 'Volvo', 29000),
            (5, 'Bentley', 350000),
            (6, 'Citroen', 21000),
            (7, 'Hummer', 41400),
            (8, 'Volkwagen', 21600),
    )

    db = sqlite3.connect(':memory:')
    db.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")

    db.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)

    for row in db.execute('SELECT * from Cars'):
        print(row)
