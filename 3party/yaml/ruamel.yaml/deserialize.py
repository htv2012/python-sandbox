"""Load from a yaml file."""

import io
import pathlib

from ruamel.yaml import YAML

USER_YAML = """
uid: 501
alias: john
shell: zsh
"""


def main():
    """Entry"""
    yaml = YAML(typ="safe")

    OBJS = [
        ("file object", open("data/user.yaml", "r")),
        ("binary file object", open("data/user.yaml", "rb")),
        ("string", USER_YAML),
        ("pathlib.Path", pathlib.Path("data/user.yaml")),
        ("io.StringIO", io.StringIO(USER_YAML)),
        ("io.Bytes", io.BytesIO(USER_YAML.encode())),
    ]
    for label, obj in OBJS:
        print(f"\n# From {label}")
        data = yaml.load(obj)
        print(data)


if __name__ == "__main__":
    main()
