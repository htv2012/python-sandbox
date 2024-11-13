#!/usr/bin/env python3
import os
import sys
import ast


class SourceParser(ast.NodeVisitor):
    def __init__(self, filename, printer=print):
        self.filename = filename
        self.printer = printer

    def start(self):
        with open(self.filename) as f:
            self.module = ast.parse(f.read(), self.filename)
            self.visit(self.module)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            function_name = node.func.id
        elif isinstance(node.func.value, ast.Name):
            function_name = node.func.attr
        else:
            return
        print(self.filename, node.lineno, function_name)

if __name__ == '__main__':
    parser = SourceParser(__file__)
    parser.start()
