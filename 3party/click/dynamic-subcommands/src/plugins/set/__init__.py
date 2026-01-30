import click

from dynamic_subcommands import MyGroup


@click.command()
@click.pass_context
def main(ctx: click.Context):
    """Set some settings"""
    print("set")
