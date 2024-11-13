#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script takes in a single parameter representing a directory
and traverse that directory to list the modules that contain errors
"""

import ast
import os
import sys


def find_error(filename):
    # Ironically, we want to ignore code that contains errors
    try:
        with open(filename) as f:
            code = f.read()
            tree = ast.parse(code, filename=filename)
    except SyntaxError as e:
        print('File: {}, error: {}, text: {}'.format(filename, e,e.text.strip()))
        # print('{}: {}'.format(e, e.text.strip()))


if __name__ == '__main__':
    sys.argv.append('.')
    root = sys.argv[1]
    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            if not filename.endswith('.py'):
                continue
            full_path = os.path.abspath(os.path.join(dirpath, filename))
            find_error(full_path)
