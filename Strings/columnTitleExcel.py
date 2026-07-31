"""
Given a string columnTitle that represents the column title as
appear in an Excel sheet, return its corresponding column number.

Example 1:
Input: columnTitle = "AZY"
Output: 1352

Example 2:
Input: columnTitle = "AB"
Output: 28

AB = A * 26^1 + B * 26^0 = 1 * 26 + 2 * 1 = 28

"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        number = 0
        pow = len(columnTitle) - 1

        for ch in columnTitle:
            idx = ord(ch) - ord("A") + 1
            number += idx * (26**pow)
            pow -= 1

        return number
