from typing import List


class Solution:
    """
    55. Jump Game
    Given an array of non-negative integers, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position.
    Determine if you are able to reach the last index.
    Example 1:
    Input: [2,3,1,1,4]
    Output: true
    """

    def canJump(self, nums: List[int]) -> bool:
        max_idx = 0
        n = len(nums)

        for i in range(n):
            curr_step = nums[i]

            if i > max_idx:
                return False

            max_idx = max(max_idx, i + curr_step)

        return True
