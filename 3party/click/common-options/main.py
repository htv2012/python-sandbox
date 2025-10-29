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
output = functools.partial(
    click.option, "--output", "-o", help="Redirect output to file"
)


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
def common(server, port, user, key_file, verbose, output):
    """Example: Using common options."""
    pass


@main.command
@add_parameters(IO)
def common_arg(output, filename):
    """Example: Common options and arguments."""
    pass


@main.command
@output(
    default="/tmp/out.txt", help="Prints to a file", show_default=True, metavar="FILE"
)
def customize(output):
    """Example: using partial to customize an option."""
    pass


if __name__ == "__main__":
    main()
