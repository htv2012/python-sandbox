import warnings
import logging
from warnings_tryout import set_level


if __name__ == '__main__':
    # This warning will print
    set_level(-1)

    # This warning will not print
    logging.captureWarnings(capture=False)
    set_level(-1)
