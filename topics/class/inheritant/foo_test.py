from test_class import TestClass


class FooTest(TestClass):
    def setup(self):
        super().setup()
        print("FooTest.setup()")


if __name__ == "__main__":
    ft = FooTest()
    ft.setup()
