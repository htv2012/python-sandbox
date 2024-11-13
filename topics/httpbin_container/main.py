import logging
import logging.config
import pathlib

from httpbin_server import HttpBin

logging.config.fileConfig(pathlib.Path(__file__).with_name("logging.ini"))


with HttpBin() as server:
    logging.info("Server started, root is %s", server.root)
    input("Press Enter to exit: ")
