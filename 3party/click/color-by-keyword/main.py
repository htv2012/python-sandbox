import click


def myecho(text: str):
    text = text.replace("[PASSED]", click.style("[PASSED]", fg="bright_green"))
    text = text.replace("[FAILED]", click.style("[FAILED]", fg="bright_red"))
    text = text.replace("[WARNING]", click.style("[WARNING]", fg="bright_yellow"))
    click.echo(text)


def main():
    myecho("test1 [PASSED]")
    myecho("test2 [FAILED]")
    myecho("test3 [WARNING]")


if __name__ == "__main__":
    main()
