import enum
from typing import Optional

import typer

app = typer.Typer()


class LogLevel(enum.Enum):
    DEBUG = "debug"
    INFO = "info"


@app.command()
def main(
    name: str,
    age: int,
    duration: float,
    formal: bool,
    tags: list[str],
    level: LogLevel,
    intro: Optional[str] = None,
):
    for name, obj in locals().items():
        print(f"{name}: {obj.__class__.__name__} = {obj!r}")


if __name__ == "__main__":
    app()
