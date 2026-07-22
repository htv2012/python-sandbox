import argparse
import json
import pathlib
import tomllib
import xml.etree.ElementTree as ET

import yaml

from . import print_tree


def main():
    parser = argparse.ArgumentParser(prog="ptree")
    parser.add_argument("path")
    options = parser.parse_args()

    path = pathlib.Path(options.path)
    if path.is_dir():
        print_tree(path)
        return

    parsers = {
        ".json": json.load,
        ".toml": tomllib.load,
        ".xml": ET.parse,
        ".yaml": yaml.safe_load,
        ".yml": yaml.safe_load,
    }
    parse = parsers.get(path.suffix)
    if parse is None:
        raise SystemExit(f"File type not supported: {path}")

    with open(options.path, "rb") as stream:
        data = parse(stream)
    print_tree(data)


if __name__ == "__main__":
    main()
