from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1

        largest = nums[0]
        l_idx = 0

        for idx, num in enumerate(nums):
            if num > largest:
                largest = num
                l_idx = idx

        for num in nums:
            if num != largest and largest < 2 * num:
                return -1

        return l_idx
