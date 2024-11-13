#!/usr/bin/env python3
import os, sys
import importlib
import logging
from inspect import getmembers, isfunction
import ast
import linecache
import pathlib
import argparse
import re


class StringVisitor(ast.NodeVisitor):
    def __init__(self, path):
        self.path = path
        self.path_as_string = str(path)

    def detect(self):
        source = path.read_text(encoding="utf-8")
        try:
            module = ast.parse(source, filename=self.path_as_string)
        except SyntaxError as exception:
            print(exception)
        else:
            self.visit(module)

    def visit_Call(self, node):
        if (
            isinstance(node.func, ast.Attribute) and
            isinstance(node.func.value, ast.Str) and
            node.func.attr == "format"
        ):
            # Skip the "...".format()
            return
        self.generic_visit(node)

    def visit_Str(self, node):
        if re.search(r'{[a-zA-Z0-9_+-:<>]+}', node.s):
            print()
            print(f"vim '+normal {node.lineno}G{node.col_offset+1}|' {self.path}")
            print(f"{self.path}:{node.lineno}:")
            print(linecache.getline(self.path_as_string, node.lineno), end="")
            print(" " * node.col_offset, end= "^\n")
        self.generic_visit(node)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=pathlib.Path)
    options = parser.parse_args()
    
    root = options.filename.resolve()
    if root.is_dir():
        paths = root.rglob("*.py")
    elif root.is_file():
        paths = [root]
    else:
        raise SystemExit(f"{options.filename} does not exist")

    for path in paths:
        visitor = StringVisitor(path)
        visitor.detect()
