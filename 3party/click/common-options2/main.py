import click


@click.group()
def main():
    pass


SERVER_OPTIONS = [
    click.option("-s", "--server", help="Host or IP"),
    click.option("-p", "--port", type=int, help="port number"),
]

USER_OPTIONS = [
    click.option("-u", "--user", help="User name"),
    click.option("-k", "--key-file", help="Path to private key file"),
]


def add_options(options):
    def _add(fn):
        for option in reversed(options):
            fn = option(fn)
        return fn

    return _add


@main.command
@add_options(SERVER_OPTIONS)
@add_options(USER_OPTIONS)
def login(server, port, user, key_file):
    """Login to a server"""
    print(f"{server=}")
    print(f"{port=}")
    print(f"{user=}")
    print(f"{key_file=}")


@main.command
@add_options(SERVER_OPTIONS)
def ping(server, port):
    """Ping a server"""
    print(f"{server=}")
    print(f"{port=}")


if __name__ == "__main__":
    main()
