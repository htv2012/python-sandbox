#!/usr/bin/env python3
import ast
import linecache
import pathlib
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("-v", "--verbose", action="store_true", default=False)
options = parser.parse_args()
filename = options.filename

with open(filename, mode="r", encoding="utf-8") as stream:
    content = stream.read()
root = ast.parse(content, filename=filename)

for node in ast.walk(root):
    if not isinstance(node, ast.FunctionDef):
        continue
    breakpoint()
    if options.verbose:
        for line_number in range(node.lineno, node.end_lineno + 1):
            line = linecache.getline(filename, line_number).rstrip()
            print(line)
            if line.endswith(":"):
                print()
                break
    else:
        print(node.name)
