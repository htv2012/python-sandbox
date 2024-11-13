"""
https://leetcode.com/problems/zigzag-conversion/description/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Example 4:
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
numRows = 7
A     M     Y     k     w
B    LN    XZ    jl    vx
C   K O   W a   i m   u y
D  J  P  V  b  h  n  t  z
E I   Q U   c g   o s
FH    RT    df    pr
G     S     e     q

Example 5:
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numRows = 5
AIQYBHJPRXZCGKOSWDFLNTVEMU

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""
import itertools


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Create numRows buckets, each bucket is a list
        buck = [[] for _ in range(numRows)]

        # Create a list of indices to insert into the buckets in zigzag order.
        indices = list(range(numRows)) + list(range(numRows - 2, 0, -1))
        indices = itertools.cycle(indices)

        # Insert the letters into the bucket in zigzag order
        for i, c in zip(indices, s):
            buck[i].append(c)

        # Construct the output string
        out = "".join(itertools.chain.from_iterable(buck))
        return out
