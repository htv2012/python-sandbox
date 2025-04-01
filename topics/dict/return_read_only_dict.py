#!/usr/bin/env python3
"""Return a read-only dict."""

from types import MappingProxyType


class BookStore:
    def __init__(self):
        # For demo
        self._price = {
            "Nobody's Boy": 17.95,
            "War and Peace": 21.95,
        }

    @property
    def price(self):
        # We don't want to return the dictionary itself because
        # we don't want others to modify it, so we return a
        # read-only proxy instead.
        return MappingProxyType(self._price)

    def update(self, title, price_in_dollars):
        self._price[title] = price_in_dollars


def main():
    """Entry"""
    book_store = BookStore()
    price_proxy = book_store.price

    print("\n# Original prices")
    for title, price in price_proxy.items():
        print(f"{title} - ${price}")

    print("\n# Attempt to modify a price")
    try:
        price_proxy["War and Peace"] = 31.95
    except TypeError as error:
        print(f"Error: {error}")

    print("\n# Verify prices still the same")
    for title, price in price_proxy.items():
        print(f"{title} - ${price}")

    print("\n# Update the price list")
    book_store.update("Nobody's Girl", 19.95)

    print("\n After update")
    for title, price in price_proxy.items():
        print(f"{title} - ${price}")


if __name__ == "__main__":
    main()
