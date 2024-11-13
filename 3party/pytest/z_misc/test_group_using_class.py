class TestNumericalFunctions:
    def test_abs(self):
        assert abs(-4) == 4

    def test_sum(self):
        assert sum([1, 2, 3]) == 6
