import click


@click.command()
@click.pass_context
def main(ctx: click.Context):
    """Read something"""
    click.echo("# get")
    click.echo(f"verbose: {ctx.obj.verbose}")
