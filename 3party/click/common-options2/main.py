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

VERBOSE = click.option(
    "-v", "--verbose", is_flag=True, default=False, help="Produce extra output"
)


def add_options(options):
    if not isinstance(options, list):
        # Turn a single parameter into a list
        options = [options]

    def _add(fn):
        for option in reversed(options):
            fn = option(fn)
        return fn

    return _add


@main.command
@add_options(SERVER_OPTIONS)
@add_options(USER_OPTIONS)
@add_options(VERBOSE)
def login(server, port, user, key_file, verbose):
    """Login to a server"""
    print(f"{server=}")
    print(f"{port=}")
    print(f"{user=}")
    print(f"{key_file=}")
    print(f"{verbose=}")
    print()


@main.command
@add_options(SERVER_OPTIONS)
@add_options(VERBOSE)
def ping(server, port, verbose):
    """Ping a server"""
    print(f"{server=}")
    print(f"{port=}")
    print(f"{verbose=}")
    print()


if __name__ == "__main__":
    main()
