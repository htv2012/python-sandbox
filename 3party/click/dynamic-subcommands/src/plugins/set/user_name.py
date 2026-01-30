import click


@click.command(name="user-name")
@click.argument("name")
@click.pass_obj
def main(obj, name):
    if obj.dryrun:
        print("[dryrun] ", end="")
    print(f"set user name to {name}")
