#!/usr/bin/env python3
from functools import partial

import click

output_format = partial(
    click.option,
    "-f",
    "--output-format",
    type=click.Choice(["json", "xml"]),
    default="json",
    help="Output format",
)


def connection_options():
    options = [
        click.option("--host"),
        click.option("--port", type=int),
    ]

    def decorate(fn):
        for option in reversed(options):
            fn = option(fn)
        return fn

    return decorate
