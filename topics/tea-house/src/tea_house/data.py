import csv
import dataclasses
import pathlib
import random
from decimal import Decimal

DATA_PATH = pathlib.Path(__file__).parent.parent / "data"


@dataclasses.dataclass
class Item:
    name: str
    price: Decimal

    @classmethod
    def from_str(cls, name: str, price: str):
        return cls(name=name, price=Decimal(price))


@dataclasses.dataclass
class Order:
    number: int
    name: str
    items: list[Item] = dataclasses.field(default_factory=list)


def load_items() -> list[Item]:
    items_path = DATA_PATH / "items.csv"
    with open(items_path) as stream:
        reader = csv.DictReader(stream)
        items = [Item.from_str(**row) for row in reader]
    return items


def generate_names():
    names_path = DATA_PATH / "names.csv"
    with open(names_path) as stream:
        names = stream.read().splitlines()

    random.shuffle(names)
    yield from names
