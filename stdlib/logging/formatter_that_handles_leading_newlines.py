import logging
import re

class MyFormatter(logging.Formatter):
    def format(self, record):
        pre_lines = 0
        while record.msg[pre_lines] == '\n':
            pre_lines += 1

        record.msg = record.msg[pre_lines:]
        formatted = ('\n' * pre_lines) + super().format(record)
        return formatted


# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger()
# logger.info('hello world')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = MyFormatter('%(levelname)s:%(name)s:%(msg)s')

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info('Hello')
logger.info('\n\nworld')