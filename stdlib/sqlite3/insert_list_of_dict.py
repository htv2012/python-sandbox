#!/usr/bin/env python3
"""
whatis: Insert list of dictionaries into a database
"""
import collections
import sqlite3


if __name__ == '__main__':
    rows = [
        {
            "codes" : "codes1",
            "distributor" : "distributor1",
            "license_type" : "license_type1",
            "duration" : "duration1",
            "one_time_usage" : "Y",
        },
        {
            "codes" : "codes2",
            "distributor" : "distributor2",
            "license_type" : "license_type2",
            "duration" : "duration2",
            "one_time_usage" : "N",
        },
    ]

    header = rows[0].keys()
    Row = collections.namedtuple('Row', header)

    db = sqlite3.connect(':memory:')
    db.execute('create table mytable ({})'.format(','.join(header)))

    db.executemany(
        'insert into mytable values (?, ?, ?, ?, ?)',
        [[r[h] for h in header] for r in rows])

    for row in map(Row._make, db.execute('select * from mytable')):
        print(row)
