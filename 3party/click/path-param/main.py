import pathlib

import click

PathStr = click.Path(
    file_okay=True,
    dir_okay=False,
    writable=True,
    resolve_path=True,
    path_type=pathlib.Path,  # Without: return str
)


@click.command
@click.option("--path", type=PathStr)
def main(path):
    print(f"{path = }")


if __name__ == "__main__":
    main()
