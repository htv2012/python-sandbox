import queue
import random
import time
from concurrent.futures import ThreadPoolExecutor

import pandas as pd
from loguru import logger

from . import Order, load_items
from .data import generate_names


def take_order(
    employees_count: int,
    names,
    items,
    customers_queue: queue.Queue,
    cash_register: list[Order],
):
    for number in range(1, 21):
        time.sleep(random.random())
        count = random.randint(1, 2)
        order = Order(
            number=number, name=next(names), items=random.sample(items, count)
        )
        customers_queue.put(order)
        cash_register.append(order)
        logger.info(
            f"Order #{order.number} from {order.name}: {', '.join(item.name for item in order.items)}"
        )

    # These are sentinels with order number < 0 to signal end of
    # queue. Each employee will receive one
    for number in range(-employees_count, 0):
        customers_queue.put(Order(number, "", []))


def prepare_drink(employee, que: queue.Queue):
    logger.info(f"{employee} start")
    drinks_count = 0  # Used for getting paid

    while True:
        order = que.get()
        if order.number < 0:
            que.task_done()
            break
        logger.info(f"Order #{order.number} assigned to {employee}")
        for item in order.items:
            logger.info(f"Order #{order.number} {employee} prepares {item.name}")
            time.sleep(random.random())
            drinks_count += 1
        logger.info(f"Order #{order.number} is ready for customer {order.name}")
        que.task_done()

    logger.info(f"{employee} done")
    return drinks_count


def report(salary, cash_register: list[Order]):
    print("\nEMPLOYEES EARNING")
    salary_df = pd.DataFrame.from_dict(salary, orient="index")
    salary_df.columns = ["Drinks Served"]
    salary_df["Earning"] = salary_df["Drinks Served"] * 0.75
    # type: ignore no-matching-overload
    salary_df.sort_values(by=["Drinks Served"], ascending=False, inplace=True)
    print(salary_df)

    orders = pd.DataFrame(
        [(item.name, item.price) for order in cash_register for item in order.items]
    )
    orders.columns = ["Item", "Price"]
    orders.set_index("Item")

    print("\nORDERS SUMMARY")
    by_sale = orders.groupby("Item").agg(
        Quantity=("Price", "count"),
        Sale=("Price", "sum"),
    )
    # type: ignore no-matching-overload
    by_sale.sort_values(by=["Sale", "Quantity"], ascending=False, inplace=True)
    print(by_sale)


def main() -> None:
    names = generate_names()
    items = load_items()
    customers_queue = queue.Queue()
    cash_register = []

    EMPLOYEES_COUNT = 5
    with ThreadPoolExecutor() as executor:
        employees = [next(names) for _ in range(EMPLOYEES_COUNT)]
        work_shift = {
            executor.submit(
                prepare_drink, employee=employee, que=customers_queue
            ): employee
            for employee in employees
        }

        executor.submit(
            take_order,
            employees_count=EMPLOYEES_COUNT,
            names=names,
            items=items,
            customers_queue=customers_queue,
            cash_register=cash_register,
        )
        customers_queue.join()
        salary = {employee: future.result() for future, employee in work_shift.items()}

    report(salary, cash_register)
