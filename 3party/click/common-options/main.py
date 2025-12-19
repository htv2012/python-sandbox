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


# Example: Shared multiple parameters
def add_parameters(*parameters):
    """Add arbitrary parameters."""

    def _add(fn):
        for option in reversed(parameters):
            fn = option(fn)
        return fn

    return _add


# ======================================================================
# main
# ======================================================================


@click.command
@add_parameters(*SERVER_OPTIONS)
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
