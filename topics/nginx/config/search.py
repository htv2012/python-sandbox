#!/usr/bin/env python3
"""Exercise the search feature."""

import pathlib

from nginx_conf_lib import (
    all_of,
    by_any_args,
    by_name,
    find_all,
    find_next,
    negative,
    parse,
)


def main():
    """Entry"""
    config_filename = pathlib.Path(__file__).with_name("nginx.conf")
    assert config_filename.exists()
    text = config_filename.read_text(encoding="utf-8")

    directives = parse(text)
    root = find_next(directives, by_name("http"))
    assert root

    print("\n# Nodes under http")
    for node in root:
        print(node)

    server_directive = find_next(root, by_name("server"))
    print("\n# Find all 'http.server.location' directives")
    for node in find_all(server_directive, by_name("location")):
        print(node)

    print("\n# Find all location that are not /")
    found = find_all(
        server_directive,
        all_of(
            by_name("location"),
            negative(by_any_args(["/"])),
        ),
    )
    for node in found:
        print(node)

    print("\n# Find location /webcomp1")
    found = find_all(
        server_directive,
        all_of(
            by_name("location"),
            by_any_args(["/webcomp1"]),
        ),
    )
    for node in found:
        print(node)


if __name__ == "__main__":
    main()
