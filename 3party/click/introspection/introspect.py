import functools
import io
from typing import Any

import click

from main import main


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


show(main)
