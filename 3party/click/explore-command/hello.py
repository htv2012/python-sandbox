from pprint import pprint

import click


@click.command(name="bar", short_help="Do the foo'lish thing")
def foo():
    """
    Do the foo'lish thing

    First will do x
    Then do y
    Finally, do z
    """
    pass


def main():
    print("\n# Inside a Command")
    pprint(vars(foo))


if __name__ == "__main__":
    main()
