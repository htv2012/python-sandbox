#!/usr/bin/env python

import csvfile

if __name__ == '__main__':
    csv_filename = 'data.csv'

    print('')
    with csvfile.list_reader(csv_filename) as csv_reader:
        for row in csv_reader:
            print(row)

    print('')
    with csvfile.dict_reader(csv_filename) as csv_reader:
        for row in csv_reader:
            print(row)
