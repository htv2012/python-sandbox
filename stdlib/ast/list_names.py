#!/usr/bin/env python3
"""
List names in a module
"""

import ast
import os
import contextlib


class Visitor(ast.NodeVisitor):
    def __init__(self, filename):
        path, _ = os.path.splitext(filename)
        with open(filename) as f:
            module = ast.parse(f.read(), path)
            self.path = path
            self.visit(module)

    @contextlib.contextmanager
    def path_descend(self, name):
        old_path = self.path
        self.path = '{}.{}'.format(self.path, name).lstrip('.')
        yield self.path
        self.path = old_path

    def visit_Name(self, node):
        print('Name:', node.id)


if __name__ == '__main__':
    visitor = Visitor('simple.py')
