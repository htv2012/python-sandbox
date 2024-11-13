# https://stackoverflow.com/a/47956442/459745
if __name__ == '__main__':
    import sqlite3

    with sqlite3.connect("testdatabase.db") as conn:
        conn.execute('DROP TABLE IF EXISTS mytable')
        conn.execute("CREATE TABLE mytable (Column1 text, Column2 text, Column3 text)")

        mytable = [
            ('a', 'b', 'c'),
            ('d', 'e', 'f'),
        ]

        for myliste in mytable:
            conn.execute("""INSERT INTO
                    mytable (Column1, Column2, Column3)
                    VALUES (?, ?, ?)""",
                myliste)
