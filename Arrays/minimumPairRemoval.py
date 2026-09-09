from typing import List


class Solution:
    def is_non_decreasing(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                return False
        return True

    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0
        nums_copy = nums.copy()
        while not self.is_non_decreasing(nums_copy):
            copy = []
            min_pair_sum = float("inf")
            min_pair_idx = 0
            for i in range(len(nums_copy) - 1):
                if nums_copy[i] + nums_copy[i + 1] < min_pair_sum:
                    min_pair_sum = nums_copy[i] + nums_copy[i + 1]
                    min_pair_idx = i

            for i in range(len(nums_copy)):
                if i == min_pair_idx + 1:
                    continue
                if i == min_pair_idx:
                    copy.append(min_pair_sum)
                else:
                    copy.append(nums_copy[i])

            nums_copy = copy
            count += 1

        return count
