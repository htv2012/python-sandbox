import jsonpath

import banner
import data


def main():
    banner.banner("Inexpensive Items")
    matches = jsonpath.query("$.products[?@.unit_price < 100]", data.inventory).select(
        "unit_price", "name"
    )
    print("Unit Price  Name")
    print("----------  ----")
    for obj in matches:
        print(f"{obj['unit_price']:>10}  {obj['name']}")

    banner.banner("Overstock")
    matches = jsonpath.query(
        "$.products[?@.inventory_count > 100]", data.inventory
    ).select("inventory_count", "name")
    print("In Stock  Name")
    print("--------  ----")
    for obj in matches:
        print(f"{obj['inventory_count']:>8}  {obj['name']}")


if __name__ == "__main__":
    main()
