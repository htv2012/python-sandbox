import click


@click.command()
@click.pass_context
def main(ctx: click.Context):
    """Send data to the cloud
    
    Write a bunch of data to the server
    """
    ctx.obj.api.put()
