import asyncio
import json
import logging
import logging.config
from pathlib import Path

import waitlib

config_file = Path(__file__).resolve().with_name("logging.ini")
logging.config.fileConfig(config_file, disable_existing_loggers=False)
logger = logging.getLogger("sample")
config_file = Path("/tmp/file.txt")


async def create_file():
    logger.debug("Start create_file")
    await asyncio.sleep(2)
    config_file.write_text('{"name": "my config"}')
    logger.debug("File created")
    return config_file


async def read_file(file):
    with open(file) as stream:
        return json.load(stream)


async def main():
    config_file.unlink(missing_ok=True)
    read_task = waitlib.wait_for_async(
        func=read_file,
        args=(config_file,),
        predicate=lambda res, exc: exc is None and res is not None,
        timeout=4,
        interval=0.5,
        logger=logger,
    )
    create_task = create_file()
    read_result, create_result = await asyncio.gather(read_task, create_task)
    logger.debug(f"{create_result = }")
    logger.debug(f"{read_result = }")


if __name__ == "__main__":
    asyncio.run(main())
