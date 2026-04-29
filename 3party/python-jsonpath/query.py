import operator

import jsonpath

import banner
import data


def show_inexpensive():
    banner.banner("Inexpensive Items")
    expr = "$.products[?@.unit_price < 100]"
    matches = jsonpath.query(expr, data.inventory).values()
    print("Unit Price  Name")
    print("----------  ----")
    for obj in matches:
        # print(f"{obj['unit_price']:>10}  {obj['name']}")
        print("{unit_price:>10}  {name}".format(**obj))


def show_overstock():
    banner.banner("Overstock")
    expr = "$.products[?@.inventory_count > 100]"
    matches = jsonpath.query(expr, data.inventory).select("inventory_count", "name")

    # Since jsonpath does not provide sort, we will sort the result ourselves
    items = sorted(matches, key=operator.itemgetter("inventory_count"), reverse=True)

    print("In Stock  Name")
    print("--------  ----")
    for obj in items:
        print("{inventory_count:>8}  {name}".format(**obj))


def main():
    show_inexpensive()
    show_overstock()


if __name__ == "__main__":
    main()
