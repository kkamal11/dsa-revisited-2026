"""
An ugly number is a positive integer whose prime factors are limited
 to 2, 3, and 5.
 Given an integer n, return True if n is an ugly number,
 or False otherwise.
 Example 1:
Input: n = 6
Output: true
Explanation: 6 = 2 x 3

Example 2:
Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
"""


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for i in [2, 3, 5]:
            while n % i == 0:
                n //= i
        return n == 1

    def get_ugly_numbers(self, n: int) -> list:
        ugly_numbers = []
        for i in range(1, n + 1):
            if self.isUgly(i):
                ugly_numbers.append(i)
        return ugly_numbers

    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1]
        i2 = i3 = i5 = 0

        for _ in range(1, n):
            next_ugly = min(
                ugly_numbers[i2] * 2, ugly_numbers[i3] * 3, ugly_numbers[i5] * 5
            )
            ugly_numbers.append(next_ugly)

            if next_ugly == ugly_numbers[i2] * 2:
                i2 += 1
            if next_ugly == ugly_numbers[i3] * 3:
                i3 += 1
            if next_ugly == ugly_numbers[i5] * 5:
                i5 += 1

        return ugly_numbers[-1]
