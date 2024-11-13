#!/usr/bin/env python3
import argparse
import shlex

VERSION = "1.0.0"


def main():
    """Entry"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--store-action", metavar="VALUE", help="Store value")
    parser.add_argument(
        "--store-const", action="store_const", const=9, help="Store a const"
    )
    parser.add_argument(
        "--store-true", dest="mybool", action="store_true", help="Store True to mybool"
    )
    parser.add_argument(
        "--store-false",
        dest="mybool",
        action="store_false",
        help="store False to mybool",
    )
    parser.add_argument(
        "--append",
        dest="flags",
        nargs="+",
        action="append",
        help="Append FLAGS to flags",
    )
    parser.add_argument(
        "--append-const",
        dest="flags",
        action="append_const",
        const="myconst",
        help="Append 'myconst' to flags",
    )
    parser.add_argument("--count", action="count", help="Count occurances of option")
    parser.add_argument("--version", action="version", version=VERSION)
    parser.add_argument("--extend", nargs="+", action="extend")
    parser.add_argument(
        "--be", action=argparse.BooleanOptionalAction, help="To be or not to be"
    )

    print("\n# Actions:")
    for action in parser._actions:
        print(f"{action.option_strings} ==> {action.__class__.__name__}")

    print("\n# Examples:")
    argvs = [
        "--store-action 'my value'",
        "--store-const",
        "--store-true",
        "--store-false",
        "--append foo bar --append moo --append-const",
        "--extend abc def ghi --extend jkl",
        "--be",
        "--no-be",
    ]

    for argv in argvs:
        print(argv)
        argv = shlex.split(argv)
        options = parser.parse_args(argv)
        print(options)
        print()


if __name__ == "__main__":
    main()
