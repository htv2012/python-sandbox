#!/usr/bin/env python3
import argparse
import pathlib
import pyclbr


def browse_function(func, indent=0):
    print(f"{indent * '    '}def {func.name}()")


def browse_class(cls, indent=0):
    print(f"class {cls.name}")
    for method in cls.children.values():
        if isinstance(method, pyclbr.Function) and not method.name.startswith("_"):
            browse_function(method, indent + 1)


def main():
    """ Entry """
    parser = argparse.ArgumentParser()
    parser.add_argument("full_path", type=pathlib.Path)
    options = parser.parse_args()

    path_to_module = str(options.full_path.parent)
    module_name = options.full_path.stem

    all_objects = pyclbr.readmodule_ex(module_name, path=[path_to_module])
    for obj in all_objects.values():
        if isinstance(obj, pyclbr.Class):
            browse_class(obj)
        elif isinstance(obj, pyclbr.Function):
            browse_function(obj)


if __name__ == '__main__':
    main()

