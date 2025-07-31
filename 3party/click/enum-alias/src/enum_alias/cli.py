import click

from .config import ConfigFile


@click.command
@click.option(
    "--config",
    type=click.Choice(ConfigFile.names(), case_sensitive=False),
    callback=ConfigFile.from_param,
    required=True,
)
def main(config) -> None:
    print(f"Name: {config}")
    print(f"Value: {config.value}")
    print(f"Path: {config.path}")
    print(f"Content: {config.content}")
    print()


if __name__ == "__main__":
    main()
