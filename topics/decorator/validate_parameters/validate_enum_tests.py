import unittest

from validate_parameters import validate_parameters


class AxisRangeType(object):
    INDEPENDENT_RANGE = 1


class OperationType(object):
    LESS_THAN = 10


class ValidateEnumTests(unittest.TestCase):
    def test_valid_argument(self):
        self._func_with_axis_range(
            AxisRangeType.INDEPENDENT_RANGE, OperationType.LESS_THAN
        )

    def test_invalid_argument(self):
        with self.assertRaises(ValueError):
            self._func_with_axis_range(AxisRangeType.INDEPENDENT_RANGE, "foo")

    def test_invalid_parameter_validation(self):
        with self.assertRaises(LookupError):
            self._func_without_operation_type(AxisRangeType.INDEPENDENT_RANGE)

    #
    # Helpers
    #
    @validate_parameters(axis_range=AxisRangeType, operation=OperationType)
    def _func_without_operation_type(self, axis_range):
        pass

    @validate_parameters(axis_range=AxisRangeType, operation=OperationType)
    def _func_with_axis_range(self, axis_range, operation):
        "Sample function for demo purpose"
        pass


if __name__ == "__main__":
    unittest.main()
