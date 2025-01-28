import datetime

import click
from prettytable import PrettyTable

from . import get_am_lich


@click.group()
def main():
    pass


@main.command()
@click.argument("year", type=int)
def nam(year):
    amlich_year = get_am_lich(year)
    click.echo(amlich_year)


@main.command()
@click.argument("con-gi", type=str.title)
def tuoi(con_gi):
    this_year = datetime.date.today().year
    rows = [
        (year, am_lich, this_year - year)
        for year in range(this_year - 120, this_year + 1)
        if con_gi in (am_lich := get_am_lich(year))
    ]

    table = PrettyTable(field_names=["Duong Lich", "Am Lich", "Tuoi"])
    table.align["Duong Lich"] = "r"
    table.align["Am Lich"] = "l"
    table.align["Tuoi"] = "r"
    table.add_rows(rows)
    click.echo(table)


if __name__ == "__main__":
    main()
