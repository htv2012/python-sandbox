import datetime

import click

from . import get_am_lich, to_vietnamese
from .tablelib import create_table


@click.group()
@click.version_option()
def main():
    pass


@main.command()
def gio():
    """Đối chiếu giờ xưa, giờ nay"""
    table = create_table(
        field_names=["Giờ Xưa", "Giờ Nay", "Chú Thích"],
        alignment="lll",
        rows=[
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
        ],
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

    table = create_table(
        field_names=["Dương Lịch", "Âm Lịch", "Số Tuổi"],
        alignment="rlr",
        rows=rows,
    )
    click.echo(table)


@main.command()
@click.option("-t", "--ten-tuoi", nargs=2, multiple=True)
def ten_tuoi(ten_tuoi):
    print(ten_tuoi)
    rows = []
    this_year = datetime.date.today().year

    for name, year in ten_tuoi:
        if name == "x":
            rows.append((" ", " ", " ", " "))
            continue
        adjustment = 0
        if year.endswith("-"):
            adjustment = -1
            year = year[:-1]
        year = int(year)
        zodiac = to_vietnamese(get_am_lich(year + adjustment))
        age = this_year - year
        rows.append((name, year, age, zodiac))

    table = create_table(
        field_names=["Tên", "Năm Sinh", "Tuổi", "Âm Lịch"],
        alignment="lrrl",
        rows=rows,
    )
    click.echo(table)


if __name__ == "__main__":
    main()
