from decimal import Decimal

from tea_house import Item


def test_from_str():
    item = Item.from_str("Classic Boba Tea", "7.25")
    assert item.name == "Classic Boba Tea"
    assert item.price == Decimal("7.25")


def test_create():
    item = Item("Classic Boba Tea", Decimal("7.25"))
    assert item.name == "Classic Boba Tea"
    assert item.price == Decimal("7.25")
