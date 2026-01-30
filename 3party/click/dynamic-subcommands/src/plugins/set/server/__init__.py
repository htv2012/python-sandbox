import pathlib

import click

from dynamic_subcommands import MyGroup

here = pathlib.Path(__file__).parent


@click.command(cls=MyGroup, plugins_dir=here)
@click.pass_obj
def main(obj):
    pass
