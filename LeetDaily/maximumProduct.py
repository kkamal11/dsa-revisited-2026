from typing import List

"""
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
Example 1: 
Input: nums = [1,2,3, -4, 5]
Output: 60
"""


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """
        we need to consider:
        i. Three largest numbers
        ii. Two smallest numbers x largest number
        """

        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
