from foo_test import FooTest
from mixin1 import Mixin1


class BarTest(FooTest, Mixin1):
    def setup(self):
        super().setup()
        print("BarTest.setup(()")


if __name__ == "__main__":
    b = BarTest()
    b.setup()

    print("\nMRO:")
    print(BarTest.__mro__)
