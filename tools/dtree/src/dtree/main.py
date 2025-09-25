#!/usr/bin/env python3


import click


@click.command
@click.option(
    "-f",
    "--filter",
    default=".",
    show_default=True,
    help=(
        "Expression to filter the result. "
        "This filter is the same filter that jq uses. "
        "See: https://jqlang.org/manual/#basic-filter"
    ),
)
@click.version_option()
@click.argument("filename", required=False, default="-")
def main(filter, filename):
    """
    Displays data file in tree format with optional jq-style filter.

    If no FILENAME, read the standard input.

    Example:

    \b
        dtree myfile.yaml
        dtree myfile.json
        dtree < myfile.yaml
        dtree myfile.yaml -f ".root.names"

    Configuration

        Configuration file is in ~/.config/dtree.toml
    """
    print(f"{filter=}")
    print(f"{filename=}")


if __name__ == "__main__":
    main()
