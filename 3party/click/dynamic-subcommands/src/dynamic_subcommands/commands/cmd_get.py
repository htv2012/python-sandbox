import click


@click.command()
@click.pass_context
def main(ctx: click.Context):
    """
    Extract data from the cloud
    
    Retrieve data from the server and display it
    """
    ctx.obj.api.get()
