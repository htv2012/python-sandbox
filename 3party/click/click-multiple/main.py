import click


@click.command
@click.option("-o", "--option", multiple=True)
def main(option):
    print(f"{option=}")


if __name__ == "__main__":
    main()
