from monotonic_stack import MonotonicStack


def main():
    s = MonotonicStack()
    for n in [1, 3, 5, 7, 6, 4]:
        s.push(n)
        print(f"Push {n} => {s}")

    print("\nPopping the stack:")
    while not s.empty:
        print(s.pop())


if __name__ == "__main__":
    main()
