#!/usr/bin/env python
import dataclasses


@dataclasses.dataclass(frozen=True)
class InventoryItem:
    name: str
    price: float
    quantity: int = dataclasses.field(default=0, repr=False)


if __name__ == "__main__":
    ii = InventoryItem("5/8 Nuts", 0.12, 10987)
    print("Inventory Item:", ii)

    ii2 = dataclasses.replace(ii, price=0.09, quantity=15)
    print("After replacement:", ii2)

    ii3 = InventoryItem(name="Small Wrench", price=15.95)
    print(f"We got {ii3.quantity} units of {ii3} left")
