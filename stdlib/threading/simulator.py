"""
Simulate such things as time consuming tasks
"""

import random
import time
from functools import wraps

import logger


def time_consuming_task(func):
    "Adds delay to a function to simulate long job"

    @wraps(func)
    def newfunc(*args):
        logger.debug("Enter %s()", func.__name__)
        time.sleep(random.randint(1, 5))
        result = func(*args)
        logger.debug("Exit %s()", func.__name__)
        return result

    return newfunc


def slackoff(slack_time=0):
    if slack_time == 0:
        slack_time = random.randint(2, 10)
    time.sleep(slack_time)
