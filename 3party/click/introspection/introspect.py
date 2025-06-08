import functools
import io
import pathlib
from typing import Any

import click

import main


def indent(n: int):
    return n * "   "


@functools.singledispatch
def show(obj: Any, level: int = 0, *args, **kwargs):
    print(f"{indent(level)}{obj}")


@show.register
def show_option(opt: click.Option, level: int = 0, *args, **kwargs):
    buf = io.StringIO()
    buf.write(indent(level))
    buf.write(f"{sorted(opt.opts)[0]} {opt.type}")
    buf.write(" \\")
    print(buf.getvalue())


@show.register
def show_group(g: click.Group, level: int = 0, *args, **kwargs):
    print(f"{g.name} \\")
    for param in g.params:
        show(param, level=level + 1)


def query_param(param: click.Parameter):
    opts = sorted(param.opts)

    print()
    print("/".join(opts))
    if param.help:
        print(param.help)

    if param.is_flag and input("Include flag, y/n? ") == "y":
        return opts[0]
    elif param.type is click.BOOL and not param.is_flag:
        ans = input("true/false/x: ")
        if ans != "x":
            return f"{opts[0]} {ans}"
    elif isinstance(param.type, click.Choice):
        choices = ["not included"] + [getattr(c, "name", c) for c in param.type.choices]
        print("Select a choice")
        print("\n".join(f"{index}. {choice}" for index, choice in enumerate(choices)))
        ans = int(input("> "))
        if ans != 0:
            return f"{opts[0]} {choices[ans]}"
    else:
        ans = input("arg: ")
        if ans != "":
            return f"{opts[0]} {ans}"


def generate_args(cli):
    for param in cli.params:
        arg = query_param(param)
        if arg:
            yield arg

    sub_commands = getattr(cli, "commands", {})
    if not sub_commands:
        return

    choices = ["No sub command"] + list(sub_commands)
    print("\n".join(f"{index}. {choice}" for index, choice in enumerate(choices)))
    ans = int(input("> "))
    if ans == 0:
        return

    ans = choices[ans]
    yield ans
    yield from generate_args(sub_commands[ans])


script = pathlib.Path(main.__file__).name
cmd = [script]
cmd.extend(generate_args(main.zt))
print(" \\\n".join(cmd))
