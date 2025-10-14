import collections


class Customer:
    def __init__(self, name, shopping_list):
        self.name = name
        self.shopping_list = collections.Counter(shopping_list)

    def purchase(self, inventory):
        for goods, amount in self.shopping_list.items():
            if 0 < amount <= inventory[goods]:
                print(f"{self.name}: purchase {amount} units of {goods}")
                inventory[goods] -= amount
                self.shopping_list[goods] -= amount

    def report(self):
        print(f"\n# {self.name}'s Shopping List")
        for goods, amount in self.shopping_list.items():
            if amount > 0:
                print(f"{amount:>3} {goods}")
