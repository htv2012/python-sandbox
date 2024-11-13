#!/usr/bin/env python
# -*- coding: utf-8 -*-


import csv
from collections import namedtuple


def import_csv(cursor, csv_reader, table_name):
    header = next(csv_reader)

    # TODO: In the future, allow the row type to be sent in as parameter
    Row = namedtuple('Row', header)

    # Create the table, ignore error (table may be existed)





if __name__ == '__main__':
    pass
