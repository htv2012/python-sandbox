from queue import PriorityQueue


def main():
    elements = [3, 5, 2, 1, 4]
    print(f"\n# Create with {elements}")
    que = PriorityQueue()
    for value in elements:
        que.put(value)

    print("\n# Retrieving")
    while not que.empty():
        print(f"- {que.get()}")


if __name__ == "__main__":
    main()
