import click


@click.command()
@click.version_option()
def main() -> None:
    print("Hello world!")
