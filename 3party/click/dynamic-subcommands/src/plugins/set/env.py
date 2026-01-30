import click


@click.command(name="env")
@click.pass_context
def main(ctx):
    print(f"Set env, dryrun={ctx.obj.dryrun}")
