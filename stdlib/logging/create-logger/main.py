#!/usr/bin/env python3

import click

from log_handlers import get_logger_filename, setup_zt_loop_logger


@click.command
@click.option(
    "--log-file",
    type=click.Path(
        file_okay=True,
        dir_okay=False,
        writable=True,
    ),
)
@click.option("--log-overwrite", is_flag=True, default=False)
@click.option("--mode", default="cowwash")
def main(log_file, log_overwrite, mode):
    filename = get_logger_filename(log_file, log_overwrite, mode)
    logger = setup_zt_loop_logger(filename)

    logger.info("Filename=%s", filename)
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")


if __name__ == "__main__":
    main()
