#!/usr/bin/env python3
import typer


app = typer.Typer()


@app.command()
def hello(name: str):
    typer.echo(f"Hello, {name}")


@app.command()
def bye(name: str, formal: bool = False):
    if formal:
        message = f"Goodbye, dear {name}"
    else:
        message = f"Bye, {name}"
    typer.echo(message)


if __name__ == "__main__":
    app()
