import enum

import click


class ServerType(enum.Enum):
    TESTING = enum.auto()
    STAGING = enum.auto()
    PILOT = enum.auto()
    PRODUCTION = enum.auto()


@click.command
@click.option(
    "-t",
    "--server-type",
    type=click.Choice(ServerType, case_sensitive=False),
    default=ServerType.TESTING,
)
def main(server_type):
    print(f"Server type: {server_type!r}")


if __name__ == "__main__":
    main()
