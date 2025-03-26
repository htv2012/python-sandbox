#!/usr/bin/env python3
"""Show imports from files"""

import argparse
import ast
from collections import defaultdict
from pathlib import Path


def find_imports(path: Path, found: dict):
    content = path.read_text()
    module = ast.parse(content, path)
    for entity in ast.walk(module):
        if isinstance(entity, ast.Import):
            for alias in entity.names:
                found[alias.name].add((path, entity.lineno))
        elif isinstance(entity, ast.ImportFrom):
            found[entity.module].add((path, entity.lineno))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir")
    options = parser.parse_args()
    root = Path(options.dir).resolve().relative_to(Path.cwd())

    if root.is_file():
        paths = [root]
    elif root.is_dir():
        paths = root.rglob("*.py")
    else:
        raise SystemExit(f"{root} is not a valid dir or file")

    found = defaultdict(set)
    for path in paths:
        find_imports(path, found)

    for mod, paths in sorted(found.items()):
        print(mod)
        for path, lineno in sorted(paths):
            print(f"  {path}({lineno})")


if __name__ == "__main__":
    main()
