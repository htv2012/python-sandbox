import argparse
import functools
import json
import pathlib
import shutil
import subprocess
import sys
from typing import Any, Dict, List, TypedDict

import yaml
import yaml.parser


class TextColor(TypedDict):
    key: str
    string_value: str
    value: str
    error: str


CONNECTOR = {True: "└── ", False: "├── "}


DEFAULT_SETTINGS = dict(
    color=TextColor(
        key="blue",
        string_value="yellow",
        value="cyan",
        error="red",
    )
)


def color_print(color: str, text: str, end: str = "\n"):
    lookup = dict(red=31, green=32, yellow=33, blue=34, megenta=35, cyan=36, white=37)
    print(f"\033[1;{lookup[color]}m{text}\033[0m", end=end)


def load_settings():
    path = pathlib.Path("~/.config/yt.yaml").expanduser()
    if not path.exists():
        with open(path, "w") as stream:
            yaml.safe_dump(
                DEFAULT_SETTINGS,
                stream=stream,
            )

    with open(path, "rb") as stream:
        settings = yaml.safe_load(stream)
    return settings


def is_scalar(obj: Any):
    return (
        obj is None
        or isinstance(obj, (int, float, str, bool))
        or obj == []
        or obj == {}
    )


def echo_value(value: Any, colors):
    if isinstance(value, str):
        color = colors["string_value"]
    else:
        color = colors["value"]
    color_print(color, repr(value))


def echo_key(key: str, color, end=None):
    color_print(color["key"], key, end=end)


def echo_index(index: int, color, end=None):
    echo_key(f"[{index}]", color, end=end)


@functools.singledispatch
def print_tree(obj: Any, color, prefix: str = ""):
    raise TypeError(f"Cannot handle object {obj!r} of type {obj.__class__.__name__}")


@print_tree.register(list)
def print_list(obj: List, color, prefix: str = ""):
    last_key = obj[-1]
    for key, value in enumerate(obj):
        last = value == last_key
        if is_scalar(value):
            print(f"{prefix}{CONNECTOR[last]}", end="")
            echo_index(key, color, end="")
            print("=", end="")
            echo_value(value, color)
        else:
            print(f"{prefix}{CONNECTOR[last]}", end="")
            echo_index(key, color)
            print_tree(value, color, f"{prefix}{'    ' if last else '│   '}")


@print_tree.register(dict)
def print_dict(obj: Dict, color, prefix: str = ""):
    last_key = list(obj)[-1]
    for key, value in obj.items():
        last = key == last_key
        if is_scalar(value):
            print(f"{prefix}{CONNECTOR[last]}", end="")
            echo_key(key, color, end="")
            print("=", end="")
            echo_value(value, color)
        else:
            print(f"{prefix}{CONNECTOR[last]}", end="")
            echo_key(key, color)
            print_tree(value, color, f"{prefix}{'    ' if last else '│   '}")


def jq(expr, tree, error_color):
    if shutil.which("jq") is None:
        return tree

    proc = subprocess.run(
        ["jq", expr],
        text=True,
        input=json.dumps(tree),
        capture_output=True,
        check=False,
    )
    if proc.stderr:
        color_print(error_color, proc.stderr)
        raise SystemExit(1)

    try:
        return yaml.safe_load(proc.stdout)
    except yaml.parser.ParserError:
        raise SystemExit(proc.stdout)


def parse(text: str):
    return yaml.safe_load(text)


def parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--filter",
        default=".",
        help=(
            "Expression to filter the result. "
            "This filter is the same as jq. "
            "See: https://jqlang.org/manual/#basic-filters"
        ),
    )
    parser.add_argument("filename", nargs="?", default="-")
    parser.add_argument("-V", "--version", action="version", version="%(PROG)s 1.1.1")
    options = parser.parse_args()
    return options


def read_file(filename: str):
    if filename == "-":
        return sys.stdin.read()
    with open(filename) as stream:
        return stream.read()


def main():
    """
    Displays a YAML file in tree format with optional JQ's style filter.

    If no FILENAME, or when FILENAME is "-", read the standard input.


    Examples

    \b
        yt myfile.yaml                         # Normal usage
        cat myfile.yaml | yt                   # Read from stdin
        yt myfile.yaml -f .venue_config.ggmas  # Filter

    Configuration

        edit ~/.config/yt.yaml
    """
    settings = load_settings()
    options = parse_command_line()
    raw = read_file(options.filename)
    tree = parse(raw)
    tree = jq(options.filter, tree, error_color=settings["color"]["error"])
    print_tree(tree, settings["color"])


if __name__ == "__main__":
    main()
