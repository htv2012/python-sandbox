import datetime

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
@click.argument("con-gi", type=str.title)
def tuoi(con_gi):
    click.echo(f"{con_gi=}")
    this_year = datetime.date.today().year
    for year in range(this_year - 120, this_year + 1):
        age = this_year - year
        amlich_year = dl_to_al(year)
        if con_gi in amlich_year:
            click.echo(f"{year}: {amlich_year}, {age} year{'s' if age>1 else ''} old")


if __name__ == "__main__":
    main()
