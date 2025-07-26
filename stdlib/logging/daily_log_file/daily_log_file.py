#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
http://stackoverflow.com/questions/30416996/change-log-file-name-in-logger-module-globally/30418499?noredirect=1#comment48929130_30418499
"""

import datetime
import os
import logging
import logging.config
import yaml


def yaml_config(yaml_filename):
    global config_dict
    with open(yaml_filename) as f:
        config_dict = yaml.load(f)

        # Append the date stamp to the file name
        logname = config_dict['handlers']['fileHandler']['filename']
        base, extension = os.path.splitext(logname)
        today = datetime.datetime.today()
        logname = '{}{}{}'.format(
            base,
            today.strftime('_%Y%m%d'),
            extension)
        config_dict['handlers']['fileHandler']['filename'] = logname

        # Apply the configuration
        logging.config.dictConfig(config_dict)


def main():
    yaml_config('daily_log_file.yaml')
    logger = logging.getLogger('default_logger')

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')


if __name__ == '__main__':
    main()
