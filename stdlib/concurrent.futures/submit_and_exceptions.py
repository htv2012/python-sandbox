#!/usr/bin/env python3
"""How to know if a function raises."""
import random
from concurrent.futures import ThreadPoolExecutor


def main():
    """Start script here."""
    input_values = [random.randint(0, 5) for _ in range(10)]
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(divmod, 100, value): value for value in input_values}

    for future, value in futures.items():
        if future.exception():
            print(f"{value} --> {future.exception()}")
        else:
            print(f"{value} --> {future.result()}")


if __name__ == "__main__":
    main()
