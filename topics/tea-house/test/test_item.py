from decimal import Decimal

from tea_house import Item


def test_item1():
    item = Item(1, "Classic Boba Tea", "7.25")
    assert item.iid == 1
    assert item.name == "Classic Boba Tea"
    assert item.price == Decimal("7.25")
