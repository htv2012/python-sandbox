from typing import Optional

import typer


def main(name: str, formal: bool, intro: Optional[str] = None):
    print(f"{name=}")
    print(f"{formal=}")
    print(f"{intro=}")


if __name__ == "__main__":
    typer.run(main)
