#!/usr/bin/env python3
import logging
import logging.config
import pathlib
import yaml


def yaml_config(filename):
    global config_dict
    with open(filename) as f:
        config_dict = yaml.load(f, Loader=yaml.FullLoader)
        logging.config.dictConfig(config_dict)

def main():
    config_filename = pathlib.Path(__file__).with_name("yaml_config.yml")
    yaml_config(config_filename)
    logger = logging.getLogger('default_logger')

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')


if __name__ == '__main__':
    main()
