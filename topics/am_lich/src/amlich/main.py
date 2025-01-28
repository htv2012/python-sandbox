import click

from . import dl_to_al


@click.group()
def main():
    pass


@main.command()
@click.argument("year", type=int)
def d2a(year):
    amlich_year = dl_to_al(year)
    click.echo(amlich_year)


@main.command()
def a2d():
    click.echo("a2d")


if __name__ == "__main__":
    main()
