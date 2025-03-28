#!/usr/bin/env python3
"""Show imports in one or more modules"""
import ast
import argparse
from pathlib import Path
from collections import defaultdict


def find_imports(path: Path, found: dict):
    if '.venv' in path.parts:
        return

    try:
        content = path.read_text()
    except FileNotFoundError:
        # Possible cause: broken symlink
        return
    try:
        root = ast.parse(content, path)
    except SyntaxError:
        return
    
    for entity in ast.walk(root):
        if isinstance(entity, ast.Import):
            for alias in entity.names:
                found[alias.name].add((path, entity.lineno))
        elif isinstance(entity, ast.ImportFrom):
            if entity.level == 0:
                # Absolute import
                found[entity.module].add((path, entity.lineno))
            else:
                # Relative import, combine the package name and module
                # Note that module could be None
                package = Path(path)
                for _ in range(entity.level):
                    package = package.parent
                package = package.name
                if entity.module:
                    package = package + "." + entity.module
                found[package].add((path, entity.lineno))


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

    for imported, imports in sorted(found.items()):
        print(f"{imported}({len(imports)})")
        for path, lineno in sorted(imports):
            print(f"  {path}:{lineno}")


if __name__ == '__main__':
    main()
