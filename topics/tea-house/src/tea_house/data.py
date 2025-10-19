import dataclasses
from decimal import Decimal


@dataclasses.dataclass
class Item:
    iid: int
    name: str
    price: Decimal

    def __post_init__(self):
        self.price = Decimal(self.price)


@dataclasses.dataclass
class Order:
    customer_name: str
    items: list[Item] = dataclasses.field(default_factory=list)
