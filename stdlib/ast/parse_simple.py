#!/usr/bin/env python3

import ast
import os


if __name__ == '__main__':
    filename = 'simple.py'
    basename = os.path.basename(__file__)
    with open(filename) as f:
        print('File: {!r}'.format(filename))
        try:
            mod = ast.parse(f.read(), basename)
            for node in ast.iter_child_nodes(mod):
                print(node)
        except SyntaxError:
            print('File contains syntax error')
