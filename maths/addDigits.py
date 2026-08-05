"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
Example 1:
Input: num = 38
Output: 2
Explanation: The process is as follows:
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.
"""


class Solution:
    def addDigits(self, num: int) -> int:
        ans = 0
        n = num

        while n > 0:  # Complexity: O(log n)
            r = n % 10
            ans += r
            n //= 10

            if n == 0 and ans >= 10:
                n = ans
                ans = 0

        return ans
