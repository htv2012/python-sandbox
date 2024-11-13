#!/usr/bin/env python3
"""Show summary of an nginx.conf file in tree format."""

import argparse
import logging
import os
import pathlib

from nginx_conf_lib import Directive, depth_first_traversal, parse

logging.basicConfig(level=os.getenv("LOGLEVEL", "WARN"))


def visit(directive: Directive, parents: tuple):
    print(len(parents) * "    ", end="")
    print(f"- {directive.name}", end="")
    print()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    options = parser.parse_args()

    config_filename = pathlib.Path(options.file)
    assert config_filename.exists()
    text = config_filename.read_text(encoding="utf-8")

    directives = parse(text)
    for directive in directives:
        depth_first_traversal(directive, visit)


if __name__ == "__main__":
    main()
