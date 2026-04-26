import json

import jsonpath


def main():
    with open("products.json") as stream:
        products = jsonpath.findall("$..products.*", stream)
    print(json.dumps(products, indent=4))


if __name__ == "__main__":
    main()
