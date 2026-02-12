#!/usr/bin/env python3
"""
Demonstrate the Norway problem: When PyYaml decode the string "NO"
(abbreviation for Norway) as No -> False.
"""

import yaml


def main():
    text_input = "NO"
    loaders = [yaml.Loader, yaml.SafeLoader, yaml.BaseLoader]
    for loader in loaders:
        data = yaml.load(text_input, Loader=loader)
        print(f"yaml.load({text_input!r}, Loader={loader.__name__}) -> {data!r}")


if __name__ == "__main__":
    main()
