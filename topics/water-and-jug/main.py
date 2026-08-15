import argparse
import collections
import itertools

from tabulate import tabulate


class Steps:
    def __init__(self):
        self.data = collections.deque()

    def prepend(self, ax, ay, note):
        self.data.appendleft({"Jug 1": ax, "Jug 2": ay, "Note": note})

    def __str__(self):
        counter = itertools.count()
        data = [{"step": next(counter), "Jug 1": 0, "Jug 2": 0, "Note": "initial"}]
        data.extend({"step": next(counter), **step} for step in self.data)

        table = tabulate(data, headers="keys", tablefmt="pipe")
        return str(table)

    def evaluate(self, target) -> str:
        jug1 = self.data[-1]["Jug 1"]
        jug2 = self.data[-1]["Jug 2"]

        if jug1 == target:
            return "Jug 1 holds the target amount"
        elif jug2 == target:
            return "Jug 2 holds the target amount"
        elif jug1 + jug2 == target:
            return "Both jugs hold the target amount"
        else:
            return "Cannot achieve target amount"


def measure(x, y, target):
    def dfs(ax, ay):
        nonlocal x, y, target, seen, steps

        if (ax, ay) in seen:
            return False
        seen.add((ax, ay))

        if ax == target or ay == target or (ax + ay) == target:
            return True

        if dfs(x, ay):
            steps.prepend(x, ax, "fill jug 1")
            return True

        if dfs(ax, y):
            steps.prepend(ax, y, "fill jug 2")
            return True

        if dfs(0, ay):
            steps.prepend(0, ay, "empty jug 1")
            return True

        if dfs(ax, 0):
            steps.prepend(ax, 0, "empty jug 2")
            return True

        amount = min(ax, y - ay)
        if dfs(ax - amount, ay + amount):
            steps.prepend(
                ax - amount, ay + amount, f"pour {amount} liters from jug 1 to jug 2"
            )
            return True

        amount = min(ay, x - ax)
        if dfs(ax + amount, ay - amount):
            steps.prepend(
                ax + amount, ay - amount, f"pour {amount} liters from jug 2 to jug 1"
            )
            return True

        return False

    seen = set()
    steps = Steps()
    dfs(0, 0)
    return steps


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=int)
    parser.add_argument("y", type=int)
    parser.add_argument("target", type=int)
    args = parser.parse_args()

    x = args.x
    y = args.y
    target = args.target

    print()
    print(f"Jug 1 can hold {x} liters")
    print(f"Jug 2 can hold {y} liters")
    print(f"We want to measure {target} liters")
    print()
    steps = measure(x, y, target)
    print(steps)
    print()
    print(steps.evaluate(target))


if __name__ == "__main__":
    main()
