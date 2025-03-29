import time
from loguru import logger
from celery import Celery

app = Celery(
    "tasks",
    backend="rpc://",
    broker="pyamqp://",
)

@app.task
def add(x, y):
    logger.info(f"Entering add, {x=}, {y=}")
    time.sleep(10)
    result = x + y
    logger.info(f"add() returns {result}")
    return result


@app.task
def user(uid):
    logger.info(f"Entering user, {uid=}")
    time.sleep(10)
    if uid == 501:
        result = {'uid': 501, 'alias': 'haiv'}
    elif uid == 502:
        result = {'uid': 502, 'alias': 'jakem'}
    else:
        raise ValueError(f"Unknown UID: {uid}")
    logger.info(f"user() returns {result}")
    return result

