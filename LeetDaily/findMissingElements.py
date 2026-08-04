from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        result = []
        nums_set = set(nums)
        mini, maxi = nums[0], nums[0]

        for num in nums:
            mini = min(mini, num)
            maxi = max(maxi, num)

        for i in range(mini, maxi + 1):
            if i not in nums_set:
                result.append(i)

        return result
