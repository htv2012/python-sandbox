#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Remove duplicate columns: the first column wins
"""

import csv
from collections import namedtuple


if __name__ == '__main__':
    with open('data.csv') as infile, open('rename_duplicated_columns_using_namedtuple.csv', 'wb') as outfile:
        reader = csv.reader(infile)
        Row = namedtuple('Row', next(reader), rename=True)
        output_header = [c for c in Row._fields if not c.startswith('_')]

        writer = csv.DictWriter(outfile, output_header, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(Row(*row)._asdict() for row in reader)
