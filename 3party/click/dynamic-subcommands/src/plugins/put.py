import click


@click.command()
@click.pass_context
def main(ctx: click.Context):
    """Write something"""
    click.echo("# put")
    click.echo(f"verbose: {ctx.obj.verbose}")
