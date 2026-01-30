import pathlib

import click

from dynamic_subcommands import MyGroup

here = pathlib.Path(__file__).parent


@click.command(cls=MyGroup, plugins_dir=here)
@click.option("-d", "--dryrun", is_flag=True, default=False)
@click.pass_context
def main(ctx: click.Context, dryrun: bool):
    """Set some settings"""
    ctx.obj.dryrun = dryrun
