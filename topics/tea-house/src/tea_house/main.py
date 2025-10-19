import queue
import random
import time
from concurrent.futures import ThreadPoolExecutor

from loguru import logger

from . import Order, load_items
from .data import generate_names


def take_order(names, items, que: queue.Queue):
    for number in range(1, 21):
        time.sleep(random.random() * 2)
        count = random.randint(1, 3)
        order = Order(
            number=number, name=next(names), items=random.sample(items, count)
        )
        logger.info(
            f"New order #{order.number} from {order.name}: {', '.join(item.name for item in order.items)}"
        )


def prepare_drink(que: queue.Queue):
    pass


def main() -> None:
    names = generate_names()
    items = load_items()
    customers_queue = queue.Queue()

    with ThreadPoolExecutor() as executor:
        executor.submit(take_order, names, items, customers_queue)
