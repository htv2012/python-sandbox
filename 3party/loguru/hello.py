from loguru import logger


def main():
    logger.critical("This is critical")
    logger.error("This is error")
    logger.warning("This is warning")
    logger.info("This is info")
    logger.debug("This is debug")
    logger.trace("This is trace")
    logger.success("This is success")


if __name__ == "__main__":
    main()
