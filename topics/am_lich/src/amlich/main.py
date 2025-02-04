import datetime

import click
from prettytable import PrettyTable

from . import get_am_lich, to_vietnamese


@click.group()
@click.version_option()
def main():
    pass


@main.command()
def gio():
    """Đối chiếu giờ xưa, giờ nay"""
    table = PrettyTable(field_names=["Giờ Xưa", "Giờ Nay", "Chú Thích"], align="l")
    table.add_rows(
        [
            ("Tí", "11PM - 01AM", "Canh ba"),
            ("Sửu", "01AM - 03AM", "Canh tư"),
            ("Dần", "03AM - 05AM", "Canh năm"),
            ("Mão", "05AM - 07AM", ""),
            ("Thìn", "07AM - 09AM", ""),
            ("Tỵ", "09AM - 11AM", ""),
            ("Ngọ", "11AM - 01PM", ""),
            ("Mùi", "01PM - 03PM", ""),
            ("Thân", "03PM - 05PM", ""),
            ("Dậu", "05PM - 07PM", ""),
            ("Tuất", "07PM - 09PM", "Canh một"),
            ("Hợi", "09PM - 11PM", "Canh hai"),
        ]
    )
    print(table)


@main.command()
@click.argument("year", type=int)
def nam(year):
    nam_am_lich = get_am_lich(year)
    nam_am_lich = to_vietnamese(nam_am_lich)
    click.echo(nam_am_lich)


@main.command()
@click.argument("con-gi", type=str.title)
def tuoi(con_gi):
    this_year = datetime.date.today().year
    rows = [
        (year, to_vietnamese(am_lich), this_year - year)
        for year in range(this_year - 120, this_year + 1)
        if con_gi in (am_lich := get_am_lich(year))
    ]

    table = PrettyTable(field_names=["Dương Lịch", "Âm Lịch", "Số Tuổi"])
    table.align["Dương Lịch"] = "r"
    table.align["Âm Lịch"] = "l"
    table.align["Số Tuổi"] = "r"
    table.add_rows(rows)
    click.echo(table)


if __name__ == "__main__":
    main()
