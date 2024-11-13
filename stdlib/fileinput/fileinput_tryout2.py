#!/usr/bin/env python
# encoding: utf-8
"""
fileinput_tryout2.py

Created by Hai Vu on 2013-02-23.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import fileinput


def process_files(file_list, out_filename):
    with open(out_filename, 'w') as fout:
        for line in fileinput.input(file_list):
            fout.write(line.rstrip()+'\n')


def main():
    files = ['data1.txt', 'data2.txt', 'data3.txt']
    process_files(files, 'example.txt')


if __name__ == '__main__':
    main()
