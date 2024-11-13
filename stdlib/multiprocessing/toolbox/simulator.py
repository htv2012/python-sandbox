"""
Simulate such things as time consuming tasks
"""

from functools import wraps
import time
import random
from .logging_lib import logger


def slackoff(max_time=8, min_time=1):
    """ Delay for a few seconds """
    slack_time = random.randint(min_time, max_time)
    time.sleep(slack_time)


def time_consuming_task(func):
    """ Simulates a time-consuming function by adding delay """

    @wraps(func)
    def inner_wrapper(*args, **kwargs):
        slackoff()
        result = func(*args, **kwargs)
        return result

    return inner_wrapper
