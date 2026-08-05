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

    def addDigits2(self, num: int) -> int:
        """
        Explanation:
        The digital root of a non-negative integer is the single digit value
        obtained by an iterative process of summing digits, on each iteration
        using the result from the previous iteration to compute a digit sum.
        The process continues until a single-digit number is reached.

        The digital root can be computed using the formula:
        digital_root(n) = 1 + (n - 1) % 9, where n is a non-negative integer.
        This can be simplified to:
        - If n == 0, then digital_root(n) = 0
        - If n % 9 == 0, then digital_root(n) = 9
        - Otherwise, digital_root(n) = n % 9
        """
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9

    def addDigitsRecusive(self, num: int) -> int:

        if num < 10:
            return num
        else:
            n = sum(int(digit) for digit in str(num))
            return self.addDigitsRecusive(n)


n = 38
sol = Solution()
print(sol.addDigits(n))
print(sol.addDigitsRecusive(n))
