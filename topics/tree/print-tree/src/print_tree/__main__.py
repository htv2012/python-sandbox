import argparse
import json
import pathlib
import xml.etree.ElementTree as ET

from . import print_tree


def main():
    parser = argparse.ArgumentParser(prog="ptree")
    parser.add_argument("path")
    options = parser.parse_args()

    path = pathlib.Path(options.path)
    if path.is_dir():
        print_tree(path)
        return

    if path.suffix == ".json":
        with open(path) as stream:
            data = json.load(stream)
    elif path.suffix == ".xml":
        data = ET.parse(path)
    else:
        raise SystemExit(f"File type not supported: {path}")
    print_tree(data)


if __name__ == "__main__":
    main()
