import logging
import logging.config
import os


here = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(here, "logging.ini")
logging.config.fileConfig(config_path)
logger = logging.getLogger("simpleExample")
