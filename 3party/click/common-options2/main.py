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

# Example: Single option to be shared
VERBOSE = click.option(
    "-v", "--verbose", is_flag=True, default=False, help="Produce extra output"
)


def log_level(levels=None, **kwargs):
    """Single option, with customization"""
    if levels is None:
        levels = ["ERROR", "WARNING", "INFO", "DEBUG"]
    return click.option("--log-level", type=click.Choice(levels), **kwargs)


def add_options(options):
    """Add arbitrary options."""
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
@log_level()
def login(server, port, user, key_file, verbose, log_level):
    """Login to a server"""
    print(f"{server=}")
    print(f"{port=}")
    print(f"{user=}")
    print(f"{key_file=}")
    print(f"{verbose=}")
    print(f"{log_level=}")
    print()


@main.command
@add_options(SERVER_OPTIONS)
@add_options(VERBOSE)
@log_level(["WARN", "INFO", "DEBUG"], default="WARN")
def ping(server, port, verbose, log_level):
    """Ping a server"""
    print(f"{server=}")
    print(f"{port=}")
    print(f"{verbose=}")
    print(f"{log_level=}")
    print()


if __name__ == "__main__":
    main()
