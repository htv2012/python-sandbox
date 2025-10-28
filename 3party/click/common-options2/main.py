import functools

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

IO = [
    click.option("--output", "-o", default="-"),
    click.argument("filename"),
]

# Example: Single option to be shared
verbose = click.option(
    "-v", "--verbose", is_flag=True, default=False, help="Produce extra output"
)

# Example: Single option using partial
output = functools.partial(click.option, "--output", "-o")


# Example: Single option, with customization
def log_level(levels=None, **kwargs):
    if levels is None:
        levels = ["ERROR", "WARNING", "INFO", "DEBUG"]
    return click.option("--log-level", type=click.Choice(levels), **kwargs)


# Example: Shared multiple options and arguments
def add_parameters(options):
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
@add_parameters(SERVER_OPTIONS)
@add_parameters(USER_OPTIONS)
@verbose
@output()
@log_level()
def login(server, port, user, key_file, verbose, log_level, output):
    """Login to a server"""
    print(f"{server=}")
    print(f"{port=}")
    print(f"{user=}")
    print(f"{key_file=}")
    print(f"{verbose=}")
    print(f"{log_level=}")
    print(f"{output=}")
    print()


@main.command
@add_parameters(SERVER_OPTIONS)
@add_parameters(verbose)
@output(default="out.txt")
@log_level(["WARN", "INFO", "DEBUG"], default="WARN")
def ping(server, port, verbose, log_level, output):
    """Ping a server"""
    print(f"{server=}")
    print(f"{port=}")
    print(f"{verbose=}")
    print(f"{log_level=}")
    print(f"{output=}")
    print()


@main.command
@add_parameters(IO)
def convert(output, filename):
    print(f"{output=}")
    print(f"{filename=}")
    print()


@main.command
@add_parameters(IO)
def unconvert(output, filename):
    print(f"{output=}")
    print(f"{filename=}")
    print()


if __name__ == "__main__":
    main()
