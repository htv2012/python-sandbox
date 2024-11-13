LOWER_BOUND = -(2**31)
UPPER_BOUND = 2**31 - 1


class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        sign = ""
        if x < 0:
            s = s[1:]
            sign = "-"

        out = int(sign + s[::-1])
        if not (LOWER_BOUND <= out <= UPPER_BOUND):
            return 0
        return out
