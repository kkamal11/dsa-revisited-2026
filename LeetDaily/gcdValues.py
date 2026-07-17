from typing import List


class Solution:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        gcd_pairs = []
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                gcd_pairs.append(self.gcd(nums[i], nums[j]))

        gcd_pairs.sort()

        return [gcd_pairs[i] for i in queries]
