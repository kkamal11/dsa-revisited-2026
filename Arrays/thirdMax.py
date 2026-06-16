from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = float("-inf")
        sec = float("-inf")
        third = float("-inf")
        nums = list(set(nums))

        n = len(nums)

        if n < 3:
            return max(nums)

        for i in range(len(nums)):
            if nums[i] > first:
                third = sec
                sec = first
                first = nums[i]
            elif nums[i] > sec:
                third = sec
                sec = nums[i]
            elif nums[i] > third:
                third = nums[i]

        return third

    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = None

        for num in nums:

            if num in (first, second, third):
                continue

            if first is None or num > first:
                third = second
                second = first
                first = num

            elif second is None or num > second:
                third = second
                second = num

            elif third is None or num > third:
                third = num

        return third if third is not None else first
