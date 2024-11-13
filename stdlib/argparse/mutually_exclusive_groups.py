#!/usr/bin/env python
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", dest="key")
    parser.add_argument("-v", "--verbose", action="store_true")

    action_group = parser.add_mutually_exclusive_group()
    action_group.required = True
    action_group.add_argument(
        "-e", "--encode", dest="action", action="store_const", const="encode",
    )
    action_group.add_argument(
        "-d", "--decode", dest="action", action="store_const", const="decode",
    )

    print(parser.parse_args())
