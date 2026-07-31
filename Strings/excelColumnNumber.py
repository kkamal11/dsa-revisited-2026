"""
Excel columns are essentially base-26 with digits 1-26 instead of 0-25,
so subtract 1 before % 26.
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        n = columnNumber

        column = []

        while n > 0:
            n -= 1
            rem = n % 26
            char = alpha[rem]
            column.append(char)
            n //= 26

        return "".join((c for c in reversed(column)))
