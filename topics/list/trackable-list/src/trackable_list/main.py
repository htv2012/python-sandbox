from .trackable_list import TrackableList


def main() -> None:
    print()
    print("Trackable List Demo")

    original = ["John", "Paul", "George", "Ringo"]
    print()
    print(f"Original list: {original}")

    # Make changes
    tracker = TrackableList(original)
    tracker[0] = "Peter"
    del tracker[-1]
    tracker[2:] = ["Mary"]

    print()
    print("Transactions are:")
    for transaction in tracker.transactions:
        print(transaction)

    print()
    print(f"List now become: {list(tracker)}")
