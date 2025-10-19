import queue
import random
import time
import typing
from concurrent.futures import ThreadPoolExecutor

import pandas as pd
from loguru import logger

from . import Order, load_items
from .data import generate_names


class Stat(typing.TypedDict):
    drink_count: int


def tally():
    # report:
    # how many drinks served
    # break down by drinks
    # how many customers
    # average drinks per customer
    # average spending per customer
    # gross, tax
    pass


def take_order(employees_count: int, names, items, que: queue.Queue):
    for number in range(1, 7):
        time.sleep(random.random() * 2)
        count = random.randint(1, 4)
        order = Order(
            number=number, name=next(names), items=random.sample(items, count)
        )
        que.put(order)
        logger.info(
            f"Order #{order.number} from {order.name}: {', '.join(item.name for item in order.items)}"
        )

    # These are sentinels with order number < 0 to signal end of
    # queue. Each employee will receive one
    for number in range(-employees_count, 0):
        que.put(Order(number, "", []))


def prepare_drink(employee, que: queue.Queue):
    logger.info(f"{employee} start")
    drinks_count = 0  # Used for getting paid

    while True:
        order = que.get()
        logger.info(f"Order #{order.number} assigned to {employee}")
        if order.number < 0:
            que.task_done()
            break
        for item in order.items:
            logger.info(f"Order #{order.number} {employee} prepares {item.name}")
            time.sleep(random.randint(3, 4))
            drinks_count += 1
        logger.info(f"Order #{order.number} is ready for customer {order.name}")
        que.task_done()

    logger.info(f"{employee} done")
    return drinks_count


def report(salary):
    salary_df = pd.DataFrame.from_dict(salary, orient="index")
    salary_df.columns = ["Drinks Served"]
    salary_df["Earning"] = salary_df["Drinks Served"] * 0.75
    print("\nEMPLOYEES EARNING")
    print(salary_df)


def main() -> None:
    names = generate_names()
    items = load_items()
    customers_queue = queue.Queue()

    with ThreadPoolExecutor() as executor:
        employees = [next(names) for _ in range(3)]
        work_shift = {
            executor.submit(
                prepare_drink, employee=employee, que=customers_queue
            ): employee
            for employee in employees
        }

        executor.submit(
            take_order, employees_count=3, names=names, items=items, que=customers_queue
        )
        customers_queue.join()
        salary = {employee: future.result() for future, employee in work_shift.items()}

    report(salary)
