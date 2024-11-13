# https://stackoverflow.com/a/47956442/459745
if __name__ == '__main__':
    import sqlite3

    conn = sqlite3.connect("testdatabase.db")
    conn.execute('DROP TABLE IF EXISTS mytable')

    # Create ['Column1', 'Column2', ..., 'Column50']
    columns = ['Column%d' % n for n in range(1, 51)]

    # Create 'Column1 TEXT, ... Column50 TEXT'
    columns_declaration = ', '.join('%s TEXT' % c for c in columns)

    conn.execute("CREATE TABLE mytable (%s)" % columns_declaration)

    conn.commit()