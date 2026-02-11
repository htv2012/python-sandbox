#!/usr/bin/env python3
"""
Demo: A YAML Loader for use which PyYaml which detects duplicated keys.
"""

import linecache

import yaml


class UniqueKeyLoader(yaml.SafeLoader):
    def construct_mapping(self, node, deep=False):
        mapping = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if key in mapping:
                raise yaml.constructor.ConstructorError(
                    f"Duplicate key detected: {key}", key_node.start_mark
                )
            mapping[key] = self.construct_object(value_node, deep=deep)
        return super().construct_mapping(node, deep=deep)


def main():
    try:
        with open("data/dup.yaml", "rb") as stream:
            yaml.load(stream, Loader=UniqueKeyLoader)
    except yaml.constructor.ConstructorError as error:
        mark = error.args[1]
        line = linecache.getline(mark.name, mark.line)
        print(error)
        print(f"{line.rstrip()} <--")


if __name__ == "__main__":
    main()
