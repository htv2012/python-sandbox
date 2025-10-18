import click

from clicklib import expand_shell_vars_callback


@click.command
@click.argument("cmd", callback=expand_shell_vars_callback)
def main(cmd):
    print(f"{cmd = }")


if __name__ == "__main__":
    main()
