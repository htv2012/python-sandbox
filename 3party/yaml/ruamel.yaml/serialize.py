"""Load from a yaml file."""

import sys

from ruamel.yaml import YAML


def main():
    """Entry"""
    yaml = YAML(typ="safe")
    data = dict(uid=501, alias="john", groups=["wheel", "users"])

    print("\n# Data")
    print(data)

    print("\n# Serialize to stdout")
    yaml.dump(data, sys.stdout)


if __name__ == "__main__":
    main()
