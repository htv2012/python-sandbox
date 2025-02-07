import click


@click.command()
@click.pass_context
def main(ctx: click.Context):
    ctx.obj.api.put()
