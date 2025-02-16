#!/usr/bin/env python3
"""
Show the internals of Result object
"""

import invoke

from explore import show_obj


def main():
    """Entry"""
    result = invoke.run("ls")
    print("\n# Result object")
    show_obj(result)


if __name__ == "__main__":
    main()
