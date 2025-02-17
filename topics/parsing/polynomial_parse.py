"""
Parse polynomial such as: 15*x-22*x**3+14*x**40
"""
from __future__ import print_function
import re
from collections import defaultdict
import unittest


def parse_polynomial(poly):
    pattern = r"""
        ([+-]?\d+)          # The coefficient
        (                   # Optionally, the x**N
            \*x             #     The X
            (               #     Optionally, the **N {
                \*\*        #         Power operator
                ([+-]?\d+)  #         The power
            )?              #     }
        )?                  # }
        """
    terms = re.findall(pattern, poly.replace(' ', ''), flags=re.VERBOSE)
    result = defaultdict(float)
    for coer, has_x, has_power, power in terms:
        coer = float(coer)
        power = float(power) if has_power else 1.0 if has_x else 0.0
        result[power] += coer

    # Optionally sort by power in decreasing order
    result = sorted(result.items(), reverse=True)
    return result


class PolyTest(unittest.TestCase):
    def test1(self):
        poly = '15*x-22*x**3+14*x**4+7-17*x**2-4*x'
        expected = [(4.0, 14.0), (3.0, -22.0), (2.0, -17.0), (1.0, 11.0), (0.0, 7.0)]
        actual = parse_polynomial(poly)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
