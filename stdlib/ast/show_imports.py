#!/usr/bin/env python3
"""Show imports in one or more modules"""
import ast
import argparse
from pathlib import Path
from collections import defaultdict


def find_imports(path: Path, found: dict):
    content = path.read_text()
    try:
        root = ast.parse(content, path)
    except SyntaxError:
        return
    
    for entity in ast.walk(root):
        if isinstance(entity, ast.Import):
            for alias in entity.names:
                found[alias.name].add((path, entity.lineno))
        elif isinstance(entity, ast.ImportFrom):
            found[entity.module].add((path, entity.lineno))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=Path)
    options = parser.parse_args()

    path = options.path
    if path.is_file():
        paths = [path]
    elif path.is_dir():
        paths = path.rglob('*.py')
    else:
        raise SystemExit(f"Expect a directory or a file, but got {path}")

    found = defaultdict(set)
    for path in paths:
        find_imports(path, found)

#    with open("/tmp/imports.json", "w") as stream:
#        import json
#        json.dump(found, stream, indent=4)
    import pprint
    pprint.pprint(found)
    breakpoint()
    for imported, imports in sorted(found.items()):
        print(imported)
        for path, lineno in sorted(imports):
            print(f"  {path}:{lineno}")


if __name__ == '__main__':
    main()
