#!/usr/bin/env python3
# whatis: scan dir and detect Python versions (2, 3) in the Python scripts
import argparse
import ast
import csv
import os
import sys

if sys.version_info.major < 3:
    raise SystemExit('This script is compatible with Python 3 or later')


def detect_version(filename):
    """
    Detects the version of a Python script and returns 2 or 3
    """
    with open(filename) as f:
        contents = f.read()
        try:
            ast.parse(contents)
            return 'python 3'
        except SyntaxError:
            return 'python 2'


def detect(dirname, excludes=set()):
    writer = csv.writer(sys.stdout)
    writer.writerow(['path', 'filename', 'version'])

    for path, dirnames, filenames in os.walk(dirname):
        path = os.path.abspath(path)
        if any(pattern in path for pattern in excludes):
            continue

        for filename in filenames:
            if not filename.endswith('.py'):
                continue
            fullpath = os.path.join(path, filename)
            try:
                version = detect_version(fullpath)
            except UnicodeDecodeError as exc:
                version = 'unknown'

            writer.writerow([path, filename, version])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dirname')
    args = parser.parse_args()

    excludes=set(['python2.', 'python3.', '\\Python27\\', 'swig\\'])
    detect(args.dirname, excludes=excludes)

if __name__ == '__main__':
    sys.exit(main())
