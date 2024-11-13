#!/usr/bin/env python
# -*- coding: utf-8 -*-


from named_tuple_csv import NamedTupleReader


if __name__ == '__main__':
    with open('users.csv') as f:
        reader = NamedTupleReader(f)

        print('Columns:', reader.fieldnames)
        print()

        for row in reader:
            print(row)
