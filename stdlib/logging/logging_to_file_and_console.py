import logging
import logging.handlers

# Log both to a file and to console: use 2 different handlers

# create logger
logger = logging.getLogger("logging_tryout2")
logger.setLevel(logging.DEBUG)

# create console handler and set appropriate level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(levelname)s: %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)

# Create a file handler and set appropriate level
fh = logging.FileHandler(filename='logging_to_file_and_console.log', mode='w')
fh.setLevel(logging.INFO)
fformatter = logging.Formatter(
    '%(asctime)s;%(filename)s(%(lineno)d);%(levelname)s;%(message)s',
    "%Y-%m-%d %H:%M:%S")
fh.setFormatter(fformatter)
logger.addHandler(fh)

# "application" code
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")

# Simulate a crash to see if log files are properly closed
# x = 5
# y = 4
# y /= x
# x /= y

logger.error("error message")
logger.critical("critical message")

# 'Cat' the log file
print('\nlogging_to_file_and_console.log:')
print((open('logging_to_file_and_console.log').read()))