#!/usr/bin/env python3
"""Class Browser Demo"""

import pyclbr


def print_class_function(desc, indent=0):
    print("    " * indent, end="")
    if isinstance(desc, pyclbr.Function):
        print("def ", end="")
    elif isinstance(desc, pyclbr.Class):
        print("class ", end="")
    print(desc.name)

    for child in desc.children.values():
        print_class_function(child, indent=indent + 1)


def main():
    print("Classes and Functions in package sample_project")

    pkg = pyclbr.readmodule_ex("sample_project", ["src"])
    for name, desc in pkg.items():
        if name == "__path__":
            continue
        print_class_function(desc)


if __name__ == "__main__":
    main()
