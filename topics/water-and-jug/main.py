import argparse


def measure(x, y, target):
    def dfs(ax, ay):
        nonlocal x, y, target, seen, steps

        if (ax, ay) in seen:
            return False
        seen.add((ax, ay))

        if ax == target or ay == target or (ax + ay) == target:
            return True

        if dfs(x, ay):
            # fill x
            steps.append(f"{x} {ay} # Fill x")
            return True

        if dfs(ax, y):
            steps.append(f"{ax} {y} # Fill y")
            return True

        if dfs(0, ay):
            steps.append(f"{0} {ay} # Empty x")
            return True

        if dfs(ax, 0):
            steps.append(f"{ax} {0} # Empty y")
            return True

        x_to_y_amount = min(ax, y - ay)
        if dfs(ax - x_to_y_amount, ay + x_to_y_amount):
            steps.append(f"{ax - x_to_y_amount} {ay + x_to_y_amount} # Transfer x -> y")
            return True

        y_to_x_amount = min(ay, x - ax)
        if dfs(ax + y_to_x_amount, ay - y_to_x_amount):
            steps.append(f"{ax + y_to_x_amount} {ay - y_to_x_amount} # Transfer y -> x")
            return True

        print()
        return False

    seen = set()
    steps = ["0 0 # Start"]
    found = dfs(0, 0)
    return found, steps


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=int)
    parser.add_argument("y", type=int)
    parser.add_argument("target", type=int)
    args = parser.parse_args()
    can_measure, steps = measure(args.x, args.y, args.target)
    if can_measure:
        print("STEPS")
        for i, step in enumerate(steps, 1):
            print(f"{i}. {step}")
    else:
        print("Cannot measure")


if __name__ == "__main__":
    main()
