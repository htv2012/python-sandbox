import queue
import random
import time
from concurrent.futures import ThreadPoolExecutor

from loguru import logger

from . import Order, load_items
from .data import generate_names
from .report import report

STOP_SIGNAL = 0


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

    # These are sentinels with order number STOP_SIGNAL to signal
    # end of queue. Each employee will receive one
    for _ in range(employees_count):
        customers_queue.put(Order(STOP_SIGNAL, "", []))


def prepare_drink(employee: str, order: Order):
    logger.info(f"Order #{order.number} assigned to {employee}")
    for item in order.items:
        logger.info(f"Order #{order.number} {employee} prepares {item.name}")
        time.sleep(random.random())
    logger.info(f"Order #{order.number} is ready for customer {order.name}")


def employee_work(employee, que: queue.Queue):
    logger.info(f"{employee} start")
    drinks_count = 0

    while True:
        order = que.get()
        if order.number == STOP_SIGNAL:
            que.task_done()
            break
        prepare_drink(employee, order)
        que.task_done()
        drinks_count += 1

    logger.info(f"{employee} done")
    return drinks_count


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
                employee_work, employee=employee, que=customers_queue
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
