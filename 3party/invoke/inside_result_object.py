#!/usr/bin/env python3
"""
A simple invoke example
"""

import reprlib

import invoke


def explore(obj, label: str):
    print(f"\n# {label}")
    for name in dir(obj):
        if name.startswith("_"):
            continue
        value = reprlib.repr(getattr(obj, name))
        print(f"- {name} = {value}")


def main():
    """Entry"""
    result = invoke.run("ls")
    explore(result, "Result object")


if __name__ == "__main__":
    main()
