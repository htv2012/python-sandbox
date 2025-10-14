from customer import Customer
from store import Store


def main():
    customers = [
        Customer("Peter", {"egg": 12, "peanut": 2}),
        Customer("Paul", {"egg": 12, "sausage": 3}),
        Customer("Mary", {"egg": 24, "sugar": 1}),
    ]

    for customer in customers:
        customer.report()

    store = Store()
    for customer in customers:
        store.add_observer(customer)

    print()
    store.add_inv("sugar", 10)
    store.add_inv("sausage", 30)
    store.add_inv("egg", 240)

    print()
    for customer in customers:
        customer.report()

    store.report()


if __name__ == "__main__":
    main()
