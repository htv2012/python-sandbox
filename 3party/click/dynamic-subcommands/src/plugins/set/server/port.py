import click


@click.command
@click.argument("port")
@click.pass_obj
def main(obj, port):
    if obj.dryrun:
        print("[dryrun] ", end="")
    print(f"set server port to {port}")
