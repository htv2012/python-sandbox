#!/usr/bin/env python3
import collections


class Store:
    def __init__(self):
        self.inv = collections.Counter()
        self.obs = []

    def add_observer(self, observer):
        self.obs.append(observer)
        observer.purchase(self.inv)

    def add_inv(self, name, count):
        print(f"store: got {count} units of {name}")
        self.inv[name] += count
        self.notify_all()

    def notify_all(self):
        for observer in self.obs:
            observer.purchase(self.inv)

    def report(self):
        print("\n# Store Inventory")
        for name, amount in self.inv.items():
            print(f"{amount:>3} {name}")
