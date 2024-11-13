from __future__ import print_function, unicode_literals
import sqlite3

con = sqlite3.connect(':memory:')
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cur.execute("INSERT INTO Cars VALUES(1, 'Audi', 52642)")
    cur.execute("INSERT INTO Cars VALUES(2, 'Mercedes', 57127)")
    
    for row in cur.execute("SELECT * FROM Cars"):
        print(row)

