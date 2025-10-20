import pandas as pd

from .data import Order


def report_earning(salary):
    print("\nEMPLOYEES EARNING")
    salary_df = pd.DataFrame.from_dict(salary, orient="index")
    salary_df.columns = ["Drinks Served"]
    salary_df["Earning"] = salary_df["Drinks Served"] * 0.75
    # type: ignore no-matching-overload
    salary_df.sort_values(by=["Drinks Served"], ascending=False, inplace=True)
    print(salary_df)


def report_order(cash_register: list[Order]):
    orders = pd.DataFrame(
        [(item.name, item.price) for order in cash_register for item in order.items]
    )
    orders.columns = ["Item", "Price"]
    orders.set_index("Item")

    print("\nORDERS SUMMARY")
    by_sale = orders.groupby("Item").agg(
        Quantity=("Price", "count"),
        Sale=("Price", "sum"),
    )
    # type: ignore no-matching-overload
    by_sale.sort_values(by=["Sale", "Quantity"], ascending=False, inplace=True)
    print(by_sale)


def report(salary, cash_register: list[Order]):
    report_earning(salary)
    report_order(cash_register)
