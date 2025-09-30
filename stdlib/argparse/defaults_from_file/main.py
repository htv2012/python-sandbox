import argparse
import collections
import contextlib
import json


def load_defaults(filename):
    with contextlib.suppress(FileNotFoundError):
        with open(filename) as stream:
            return json.load(stream)
    return {}


def save_defaults(defaults, filename):
    with open(filename, "w") as stream:
        json.dump(defaults, stream, indent=4)


def main():
    defaults = collections.ChainMap(
        load_defaults("last.json"),
        load_defaults("defaults.json"),
    )

    parser = argparse.ArgumentParser()
    parser.set_defaults(**defaults)
    parser.add_argument("--foo")
    parser.add_argument("--bar")

    options = parser.parse_args()
    save_defaults(options.__dict__, "last.json")

    print(options)


if __name__ == "__main__":
    main()
