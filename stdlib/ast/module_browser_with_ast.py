#!/usr/bin/env python3
import argparse
import pathlib
import ast


class ModuleVisitor(ast.NodeVisitor):
    def __init__(self, module):
        self.parents = [module]

    def show_parents(self):
        print(".".join(self.parents), end=".")

    def visit_ClassDef(self, node):
        # print(f"class {node.name}")
        self.parents.append(node.name)
        self.generic_visit(node)
        self.parents.pop()

    def visit_FunctionDef(self, node):
        if node.name.startswith("_"):
            return

        self.show_parents()
        print(f"{node.name}")


def parse_module(full_path, root):
    contents = full_path.read_text()
    r = ast.parse(contents, filename=str(full_path))
    v = ModuleVisitor(f"{root}.{full_path.stem}")
    v.visit(r)


def find_package(path):
    if not path.is_dir():
        path = path.parent
    path = pathlib.Path(path).resolve()
    components = []

    while (path / "__init__.py").exists():
        components.insert(0, path.name)
        path = path.parent

    return '.'.join(components)


def main():
    """ Entry """
    parser = argparse.ArgumentParser()
    parser.add_argument("full_path", type=pathlib.Path)
    options = parser.parse_args()
    root = find_package(options.full_path)
    parse_module(options.full_path, root)


if __name__ == '__main__':
    main()

