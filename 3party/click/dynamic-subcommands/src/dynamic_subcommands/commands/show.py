import click


@click.group()
@click.option(
    "-f", "--output-format", type=click.Choice(["json", "xml"]), default="json"
)
@click.pass_context
def main(ctx: click.Context, output_format):
    """Show information"""
    ctx.obj.output_format = output_format


@main.command(name="root")
@click.pass_context
def show_root(ctx):
    """Show the root"""
    click.echo("# show root")
    click.echo(f"output format: {ctx.obj.output_format}")
    click.echo(f"verbose: {ctx.obj.verbose}")
