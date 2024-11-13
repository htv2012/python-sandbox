#!/usr/bin/env python
# encoding: utf-8
"""
fileinput_tryout1.py

Created by Hai Vu on 2013-02-05.
Copyright (c) 2013 High View Software. All rights reserved.

Demo: using fileinput to 'grep' for files in a directory
"""

import sys
import os
import fileinput


def simple_fgrep(search_term, search_dir):
    '''
    Searchs files in a directory for text.
    Returns a list of tupples: (filename, line_number, line)
    '''
    os.chdir(search_dir)
    input_files = (f for f in os.listdir('.') if os.path.isfile(f))
    output_files = []
    for line in fileinput.input(input_files):
        line = line.strip()
        if search_term in line:
            result = fileinput.filename(), fileinput.filelineno(), line
            output_files.append(result)
            fileinput.nextfile()
    return output_files

if __name__ == '__main__':
    for filename, line_number, line in simple_fgrep('haiv', '/Users/haiv/src/python'):
        print('{0}({1}): {2}'.format(filename, line_number, line))
