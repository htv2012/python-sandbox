import csv
import dataclasses
import pathlib
from decimal import Decimal


@dataclasses.dataclass
class Item:
    iid: int
    name: str
    price: Decimal

    def __post_init__(self):
        self.iid = int(self.iid)
        self.price = Decimal(self.price)


@dataclasses.dataclass
class Order:
    customer_name: str
    items: list[Item] = dataclasses.field(default_factory=list)


def load_items() -> list[Item]:
    data_path = pathlib.Path(__file__).parent.parent / "data" / "items.csv"
    with open(data_path) as stream:
        reader = csv.DictReader(stream)
        items = [Item(**row) for row in reader]
    return items
