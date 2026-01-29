import _common_parameters
import click


@click.group()
@click.pass_context
def main(ctx: click.Context):
    """Show information"""
    pass


@main.command(name="root")
@_common_parameters.output_format()
@click.pass_context
def show_root(ctx, output_format):
    """Show the root."""
    click.echo("# show root")
    click.echo(f"output format: {output_format}")
    click.echo(f"verbose: {ctx.obj.verbose}")


@main.command(name="env")
@_common_parameters.output_format(default="xml", show_default=True)
@click.pass_context
def show_env(ctx, output_format):
    """Show the environment variables."""
    click.echo("# show env")
    click.echo(f"output format: {output_format}")
    click.echo(f"verbose: {ctx.obj.verbose}")


@main.command(name="connection")
@_common_parameters.output_format()
@_common_parameters.connection_options()
@click.pass_context
def show_connection(ctx, host, port, output_format):
    """Show the connection."""
    click.echo("# show connection")
    click.echo(f"host: {host}")
    click.echo(f"port: {port}")
    click.echo(f"output format: {output_format}")
    click.echo(f"verbose: {ctx.obj.verbose}")
