from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sum_ = 0
        n = len(nums)

        for i in range(n):
            max_ = float("-inf")
            min_ = float("inf")
            for j in range(i, n):
                max_ = max(max_, nums[j])
                min_ = min(min_, nums[j])
                sum_ += max_ - min_

        return sum_


sol = Solution()
arr = [1, 2, 3]
print(sol.subArrayRanges(arr))
