import csv
import decimal
import pathlib


def process(row: dict):
    amount = decimal.Decimal(row["Amount"])
    tip_percent = decimal.Decimal(row["Tip"])
    tax_percent = decimal.Decimal(row["Tax"])
    total = amount + tax_percent * amount + tip_percent * amount
    print()
    print(f"Amount: {amount}")
    print(f"Tax:    {tax_percent}")
    print(f"Tip:    {tip_percent}")
    print(f"Total:  {total}")


def main():
    print("\n# Decimal vs Floating")

    decimal.getcontext().prec = 2

    data_path = pathlib.Path(__file__).parent / "data" / "transactions.csv"
    with open(data_path) as stream:
        reader = csv.DictReader(stream)
        for row in reader:
            process(row)


if __name__ == "__main__":
    main()
