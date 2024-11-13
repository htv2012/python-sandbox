"""
For a given stock, we are given a list of stock prices that increment every minute. For example:

Prices(p): [4, 5, 9, 5, 3, 9, 2, 6]

Determine the biggest profit you can make through one buy and one sell
Solution: Buy at t=4, Sell at t=5, Profit = t(5) - t(4) = 9 - 3 = 6

"""

import logging
import os

logging.basicConfig(level=os.getenv("LOGLEVEL", "WARNING"))


def calculate_max_profit(prices: list[int]) -> int:
    prices = iter(prices)
    max_profit = 0
    smallest = previous_price = next(prices)
    for price in prices:
        logging.debug(
            "smallest=%r, previous_price=%r, price=%r", smallest, previous_price, price
        )
        max_profit = max(price - smallest, max_profit)
        if price - previous_price < 0:
            smallest = min(smallest, price)

    return max_profit
