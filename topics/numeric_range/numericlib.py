import dataclasses


@dataclasses.dataclass(frozen=True)
class NumericRange:
    """Implement a numeric range.

    Convert to string:

        >>> str(NumericRange(1001, 3))
        '1001-1003'

    Convert to list:

        >>> list(NumericRange(1001, 3))
        [1001, 1002, 1003]

    Convert to int, only applicable to range with count == 1:

        >>> int(NumericRange(10001))
        10001

    Membership:

        >>> 1002 in NumericRange(1001, 3)
        True

        >>> 1004 in NumericRange(1001, 3)
        False

    More Example:

        ports = NumericRange(1001, count=3)
        for port in ports:
            print(port)

        Output:
        1001
        1002
        1003
    """

    start: int
    count: int = 1

    @classmethod
    def from_str(cls, range_str):
        """Convert range such as '10001-10005` to NumericRange.

        >>> NumericRange.from_str("10001-10005")
        NumericRange(start=10001, count=5)
        """
        start_value, end_value = [int(value) for value in range_str.split("-")]
        return cls(start=start_value, count=end_value - start_value + 1)

    def __str__(self):
        """Return string presentation, e.g. '1001-1003'."""
        if self.count == 1:
            return str(self.start)
        return f"{self.start}-{self.start + self.count - 1}"

    def __iter__(self):
        yield from range(self.start, self.start + self.count)

    def __int__(self):
        if self.count == 1:
            return self.start
        raise TypeError(f"Cannot convert range with count > 1: {self!r}")
