import functools
import json
import pathlib
import shutil
import subprocess
from typing import Any, Dict, List

import click
import yaml
import yaml.parser

CONNECTOR = {True: "└── ", False: "├── "}

KEY_COLOR = "key"
STRING_VALUE_COLOR = "string_value"
VALUE_COLOR = "value"
ERROR_COLOR = "error"

DEFAULT_SETTINGS = {
    "color": {
        KEY_COLOR: "bright_blue",
        STRING_VALUE_COLOR: "bright_yellow",
        VALUE_COLOR: "bright_cyan",
        ERROR_COLOR: "red",
    }
}


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


def echo_value(value: Any, color):
    click.secho(
        repr(value),
        fg=color[STRING_VALUE_COLOR] if isinstance(value, str) else color[VALUE_COLOR],
    )


def echo_key(key: str, color, nl=True):
    click.secho(key, fg=color[KEY_COLOR], nl=nl)


def echo_index(index: int, color, nl=True):
    echo_key(f"[{index}]", color, nl=nl)


@functools.singledispatch
def print_tree(obj: Any, color, prefix: str = ""):
    raise TypeError(f"Cannot handle object {obj!r} of type {obj.__class__.__name__}")


@print_tree.register(list)
def print_list(obj: List, color, prefix: str = ""):
    last_key = obj[-1]
    for key, value in enumerate(obj):
        last = value == last_key
        if is_scalar(value):
            click.echo(f"{prefix}{CONNECTOR[last]}", nl=False)
            echo_index(key, color, nl=False)
            click.echo("=", nl=False)
            echo_value(value, color)
        else:
            click.echo(f"{prefix}{CONNECTOR[last]}", nl=False)
            echo_index(key, color)
            print_tree(value, color, f"{prefix}{'    ' if last else '│   '}")


@print_tree.register(dict)
def print_dict(obj: Dict, color, prefix: str = ""):
    last_key = list(obj)[-1]
    for key, value in obj.items():
        last = key == last_key
        if is_scalar(value):
            click.echo(f"{prefix}{CONNECTOR[last]}", nl=False)
            echo_key(key, color, nl=False)
            click.echo("=", nl=False)
            echo_value(value, color)
        else:
            click.echo(f"{prefix}{CONNECTOR[last]}", nl=False)
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
        click.secho(proc.stderr, fg=error_color)
        raise SystemExit(1)

    try:
        return yaml.safe_load(proc.stdout)
    except yaml.parser.ParserError:
        raise SystemExit(proc.stdout)


def parse(text: str):
    return yaml.safe_load(text)


@click.command
@click.option(
    "-f",
    "--filter",
    default=".",
    show_default=True,
    help=(
        "Expression to filter the result. "
        "This filter is the same as jq. "
        "See: https://jqlang.org/manual/#basic-filters"
    ),
)
@click.version_option()
@click.argument("filename", required=False, default="-")
def main(filter, filename) -> None:
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
    with click.open_file(filename or "-") as stream:
        raw = stream.read()
    tree = parse(raw)
    tree = jq(filter, tree, error_color=settings["color"][ERROR_COLOR])
    print_tree(tree, settings["color"])


if __name__ == "__main__":
    main()
