import functools

import click


@click.group()
def main():
    pass


SERVER_OPTIONS = [
    click.argument("server"),
    click.option("-p", "--port", type=int, help="port number"),
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
@verbose
@output()  # For partial, the parentheses are required
def common(server, port, verbose, output):
    """Example: Using common options and arguments."""
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
