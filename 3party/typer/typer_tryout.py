#!/usr/bin/env python3
import typer


def main(name):
    typer.echo(f"Hello, {name}")


if __name__ == "__main__":
    typer.run(main)
