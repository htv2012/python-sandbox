#!/usr/bin/env python
import logging
import logging.config
import multiprocessing

import config
import stuff


logging.config.fileConfig("logging.ini")



def main():
    """ Entry """
    logger = logging.getLogger("config")
    logger.info(f"Config: {config.name}")

    logger.info("Change name to 'prod'")
    config.name = "prod"
    logger.info(f"Config: {config.name}")

    process = multiprocessing.Process(
        name="stuff.perform",
        target=stuff.perform,
    )
    process.start()
    process.join()


    logger.info("Back to main")
    logger.info(f"Config: {config.name}")


if __name__ == '__main__':
    main()
