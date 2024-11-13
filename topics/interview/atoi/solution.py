LOWER_BOUND = -(2**31)
UPPER_BOUND = 2**31 - 1
ZERO = ord("0")


class Solution:
    def myAtoi(self, s: str) -> int:
        # Strip leading spaces
        buf = s.lstrip(" ")
        if buf == "":
            return 0

        # Determine the sign
        sign = 1
        if buf[0] == "-":
            sign = -1
            buf = buf[1:]
        elif buf[0] == "+":
            buf = buf[1:]

        # Collect the digits and convert to int, one digit at
        # at time
        out = 0
        for ch in buf:
            digit = ord(ch) - ZERO
            if 0 <= digit <= 9:
                out = out * 10 + digit
            else:
                # Not a digit character
                break

        # Adjust the sign
        out = out * sign

        # Check for 32-bit int bound
        if out < LOWER_BOUND:
            out = LOWER_BOUND
        elif out > UPPER_BOUND:
            out = UPPER_BOUND
        return out
