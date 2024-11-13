#!/usr/bin/env python

import json
import sqlite3

if __name__ == '__main__':
    # Create an in-memory database for calculation
    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS time_table')
    cursor.execute('CREATE TABLE time_table (name text, time real)')
    connection.commit()

    # Load file into database
    with open('raw.json') as f:
        for line in f:
            row = json.loads(line)
            cursor.execute('INSERT INTO time_table VALUES (?,?)', (row['name'], row['time']))
            connection.commit()

    # Prints the whole table, sum, average, sorted by name
    cursor.execute('SELECT name, COUNT(time), SUM(time), AVG(time) FROM time_table GROUP BY name')
    print('%-10s %8s %8s %8s' % ('NAME', 'COUNT', 'SUM', 'AVERAGE'))
    for row in cursor.fetchall():
        print('%-10s %8d %8.2f %8.2f' % row)
    
    connection.close()

