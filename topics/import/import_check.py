#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
import ast
import argparse

class Scanner(ast.NodeVisitor):
    def visit_Import(self, node):
        global n
        n = node
        print(node)
        print(ast.dump(node, include_attributes=True))
        print('---')

def import_checker(filename):
    with open(filename) as f:
        contents = f.read()
        root_node = ast.parse(contents, filename=filename)
        scanner = Scanner()
        scanner.visit(root_node)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    options = parser.parse_args()
    print(import_checker(options.filename))
