"""
whatis: How to create a logging object which has different formatting for debug?
"""
import logging


class DebugLogger(logging.Logger):
    def debug(self, msg, *args, **kwargs):
        if self.isEnabledFor(logging.DEBUG):
            self._log(logging.DEBUG, "==> " + msg, args, **kwargs)


if __name__ == '__main__':
    # Temporarily replace the default logger with our custom one, then
    # create a new logger object
    existing_logger_class = logging.getLoggerClass()
    logging.setLoggerClass(DebugLogger)

    logger = logging.getLogger(__name__)

    logging.setLoggerClass(existing_logger_class)

    # Create handler as normal
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    logger.addHandler(handler)

    # Start logging
    logger.error('This is error')
    logger.warning('This is warn')
    logger.info('This is info')
    logger.debug('This is debug')
