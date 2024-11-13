#!/usr/bin/env python3
class Solution:
    def intToRoman(self, num: int) -> str:
        """1 <= num <= 3999"""
        assert 1 <= num <= 3999, f"Invalid input: {num}"

        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        thousand, rem = divmod(num, 1000)
        hundred, rem = divmod(rem, 100)
        ten, one = divmod(rem, 10)

        return f"{m[thousand]}{c[hundred]}{x[ten]}{i[one]}"
