import click


@click.command()
@click.pass_context
def main(ctx: click.Context):
    """Get status"""
    click.echo("# get-status")
    click.echo(f"verbose: {ctx.obj.verbose}")
