import enum
import sys

import click
from loguru import logger


class ExitStyle(enum.Enum):
    NORMAL = enum.auto()
    RAISE = enum.auto()
    CTX_FAIL = enum.auto()
    CTX_EXIT_0 = enum.auto()
    CTX_EXIT_1 = enum.auto()
    CTX_ABORT = enum.auto()
    SYS_EXIT_0 = enum.auto()
    SYS_EXIT_1 = enum.auto()


class MyResource:
    def __enter__(self):
        logger.info("Prepare resource")

    def __exit__(self, exc_type, exc_value, tb):
        logger.info("Clean up resource")


@click.group()
@click.pass_context
def main(ctx):
    logger.info("Start main")
    ctx.obj = ctx.with_resource(MyResource())


@main.command()
@click.option(
    "-e",
    "--exit-style",
    type=click.Choice(ExitStyle, case_sensitive=False),
    default=ExitStyle.NORMAL,
)
@click.pass_context
def sub(ctx, exit_style):
    logger.info("Inside sub")
    logger.info(f"Exit Style: {exit_style}")

    if exit_style == ExitStyle.NORMAL:
        return
    elif exit_style == ExitStyle.RAISE:
        raise RuntimeError("Out of coffee")
    elif exit_style == ExitStyle.CTX_FAIL:
        ctx.fail("Out of milk")
    elif exit_style == ExitStyle.CTX_EXIT_0:
        ctx.exit(0)
    elif exit_style == ExitStyle.CTX_EXIT_1:
        ctx.exit(1)
    elif exit_style == ExitStyle.CTX_ABORT:
        ctx.abort()
    elif exit_style == ExitStyle.SYS_EXIT_0:
        sys.exit(0)
    elif exit_style == ExitStyle.SYS_EXIT_1:
        sys.exit(1)


if __name__ == "__main__":
    main()
