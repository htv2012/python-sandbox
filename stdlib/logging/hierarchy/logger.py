#!/usr/bin/env python3
import logging
import logging.config
import pathlib

import yaml


config_filename = pathlib.Path(__file__).with_name("log_config.yaml")
with open(config_filename) as stream:
    config_dict = yaml.load(stream, Loader=yaml.FullLoader)
    logging.config.dictConfig(config_dict)
    logger = logging.getLogger("app")

