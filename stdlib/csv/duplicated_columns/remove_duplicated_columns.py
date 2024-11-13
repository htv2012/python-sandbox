#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Remove duplicate columns: the first column wins
"""

import csv
from collections import namedtuple


def mark_duplicate_columns(header):
    output_header = []
    for column in header:
        if column in output_header:
            column = '_dup_' + column
        output_header.append(column)
    return output_header


if __name__ == '__main__':
    with open('data.csv') as infile, open('rename_duplicated_columns.csv', 'wb') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        header = mark_duplicate_columns(next(reader))
        for row in reader:
            row = [f for c, f in zip(header, row) if '_dup_' not in c]
        writer.writerows(Row(*row)._asdict() for row in reader)
