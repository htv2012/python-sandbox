#!/usr/bin/env python3
"""Show imports frequencies"""

import argparse
import ast
from collections import Counter
from pathlib import Path


def find_imports(path: Path, counter: dict):
    if ".venv" in path.parts:
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
                counter.update([alias.name])
        elif isinstance(entity, ast.ImportFrom):
            if entity.level == 0:
                # Absolute import
                counter.update([entity.module])
            else:
                # Relative import, combine the package name and module
                # Note that module could be None
                package = Path(path)
                for _ in range(entity.level):
                    package = package.parent
                package = package.name
                if entity.module:
                    package = package + "." + entity.module
                counter.update([package])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    options = parser.parse_args()

    path = options.path
    if path.is_file():
        paths = [path]
    elif path.is_dir():
        paths = path.rglob("*.py")
    else:
        raise SystemExit(f"Expect a directory or a file, but got {path}")

    counter = Counter()
    for path in paths:
        find_imports(path, counter)

    for mod, count in counter.most_common():
        print(f"{count:>3} {mod}")


if __name__ == "__main__":
    main()
