import functools

import click

SERVER_OPTIONS = [
    click.argument("server"),
    click.option(
        "-p", "--port", type=int, help="port number", default=8888, show_default=True
    ),
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


# ======================================================================
# main
# ======================================================================


@click.command
@add_parameters(SERVER_OPTIONS)
@verbose
@output(
    default="/tmp/out.txt", help="Prints to a file", show_default=True, metavar="FILE"
)
def main(server, port, verbose, output):
    """Common Options Demo"""
    print(f"{server = }")
    print(f"{port = }")
    print(f"{output = }")
    print(f"{verbose = }")
    print()


if __name__ == "__main__":
    main()
