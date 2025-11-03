#!/usr/bin/env python3
import argparse
import csv
import os.path
import pathlib
import pyclbr


def parse(path: pathlib.Path):
    path_to_module = path.parent
    module_name = path.stem
    try:
        return pyclbr.readmodule_ex(module_name, path=[str(path_to_module)])
    except ValueError as err:
        if ".__spec__ is None" not in str(err):
            raise
        # module_name = f"{path_to_module.name}.{module_name}"
        # path_to_module = path_to_module.parent
        module_name = f"{path.parent.name}.{path.stem}"
        path_to_module = path.parent.parent
        print(f"{path=}")
        print(f"{path_to_module=}")
        print(f"{module_name=}")
        return pyclbr.readmodule_ex(module_name, path=[str(path_to_module)])


def get_name(obj):
    parts = []
    while obj is not None:
        try:
            parts.insert(0, obj.name)
        except Exception as err:
            breakpoint()
        obj = obj.parent

    return ".".join(parts)


def report(obj):
    name = get_name(obj)
    file = os.path.normpath(obj.file)
    yield name, file, obj.lineno

    for child in obj.children.values():
        yield from report(child)


def parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=pathlib.Path)
    options = parser.parse_args()
    root = options.root.expanduser().resolve()
    assert root.exists()
    assert root.is_dir()
    return root


def find_definitions(root: pathlib.Path):
    for path in root.rglob("*.py"):
        if "/.venv/" in str(path):
            continue
        try:
            result = parse(path)
        except SyntaxError:
            continue
        for obj in result.values():
            yield from report(obj)


def main():
    root = parse_command_line()
    with open("tags.csv", "w") as stream:
        writer = csv.writer(stream)
        writer.writerow(("name", "file", "lineno"))
        writer.writerows(find_definitions(root))


if __name__ == "__main__":
    main()
