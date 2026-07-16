from typing import List


class Solution:
    def gcd(self, a: int, b: int) -> int:
        """Time complexity is O(log(min(a, b)))"""
        while b != 0:
            a, b = b, a % b
        return a

    def gcdSum(self, nums: list[int]) -> int:
        prefix_gcd = []
        mxi = float("-inf")

        for num in nums:
            mxi = max(mxi, num)
            prefix_gcd.append(self.gcd(num, mxi))

        prefix_gcd.sort()

        n = len(prefix_gcd)
        result = 0

        for start in range(n // 2):
            end = n - start - 1
            if start != end:
                result += self.gcd(prefix_gcd[start], prefix_gcd[end])

        return result
