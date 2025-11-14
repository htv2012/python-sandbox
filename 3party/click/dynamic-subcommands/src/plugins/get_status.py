import click


@click.command()
@click.pass_obj
def main(obj):
    """Get status"""
    click.echo("# get-status")
    click.echo(f"verbose: {obj.verbose}")
