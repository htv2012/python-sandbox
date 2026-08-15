import argparse
import collections
import itertools

from tabulate import tabulate


class Steps:
    def __init__(self):
        self.data = collections.deque()

    def prepend(self, jug1, jug2, note):
        self.data.appendleft({"Jug 1": jug1, "Jug 2": jug2, "Note": note})

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


def measure(jug1_max, jug2_max, target):
    def dfs(jug1, jug2):
        nonlocal jug1_max, jug2_max, target, seen, steps

        if (jug1, jug2) in seen:
            return False
        seen.add((jug1, jug2))

        if jug1 == target or jug2 == target or (jug1 + jug2) == target:
            return True

        if dfs(jug1_max, jug2):
            steps.prepend(jug1_max, jug1, "fill jug 1")
            return True

        if dfs(jug1, jug2_max):
            steps.prepend(jug1, jug2_max, "fill jug 2")
            return True

        if dfs(0, jug2):
            steps.prepend(0, jug2, "empty jug 1")
            return True

        if dfs(jug1, 0):
            steps.prepend(jug1, 0, "empty jug 2")
            return True

        amount = min(jug1, jug2_max - jug2)
        if dfs(jug1 - amount, jug2 + amount):
            steps.prepend(jug1 - amount, jug2 + amount, "pour jug 1 to jug 2")
            return True

        amount = min(jug2, jug1_max - jug1)
        if dfs(jug1 + amount, jug2 - amount):
            steps.prepend(jug1 + amount, jug2 - amount, "pour jug 2 to jug 1")
            return True

        return False

    seen = set()
    steps = Steps()
    dfs(0, 0)
    return steps


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("jug1_max", type=int)
    parser.add_argument("jug2_max", type=int)
    parser.add_argument("target", type=int)
    args = parser.parse_args()

    jug1_max = args.jug1_max
    jug2_max = args.jug2_max
    target = args.target

    print()
    print(f"Jug 1 can hold {jug1_max} liters")
    print(f"Jug 2 can hold {jug2_max} liters")
    print(f"We want to measure {target} liters")
    print()

    steps = measure(jug1_max, jug2_max, target)
    print(steps)
    print()
    print(steps.evaluate(target))


if __name__ == "__main__":
    main()
