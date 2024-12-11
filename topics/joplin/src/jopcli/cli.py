import click

from . import db


@click.group()
def main():
    pass


@main.command()
@click.argument("title")
def cat(title):
    with db.connect() as connection:
        for row_dict in db.search_by_title(connection, title):
            click.echo(row_dict["body"])


@main.command()
def ls():
    with db.connect() as connection:
        for (title,) in connection.execute("select title from notes"):
            print(title)


@main.command()
@click.argument("terms", nargs=-1)
def search(terms):
    with db.connect() as connection:
        for (title,) in db.search(connection, terms, columns_csv="title"):
            print(title)
