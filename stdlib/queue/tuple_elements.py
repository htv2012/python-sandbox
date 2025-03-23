from queue import PriorityQueue


def print_task(priority, description):
    print(f"{priority}. {description}")


def main():
    print("\n# Insert")

    elements = [
        (5, "Play guitar"),
        (3, "Prepare dinner"),
        (4, "Wash Fido"),
        (1, "Grocery shopping"),
        (2, "Take car to the shop"),
    ]
    que = PriorityQueue()
    for value in elements:
        print_task(*value)
        que.put(value)

    print("\n# Retrieve")
    while not que.empty():
        priority, description = que.get()
        print_task(priority, description)


if __name__ == "__main__":
    main()
