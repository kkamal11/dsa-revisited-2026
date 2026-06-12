from typing import List
import random

"""
Given an array of integers with possible duplicates, randomly output the 
index of a given target number. You can assume that the given 
target number must exist in the array.

Example 1:
Input: ["Solution","pick","pick","pick"]
[[[1,2,3,3,3]],[3],[3],[3]]
Output: [null,4,2,3]
"""


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.mapp = {}
        for i, num in enumerate(self.nums):
            if num not in self.mapp:
                self.mapp[num] = []
            self.mapp[num].append(i)

    def pick(self, target: int) -> int:
        """This is like round robin"""
        idx = self.mapp[target].pop(0)
        self.mapp[target].append(idx)
        return idx

    def pick(self, target: int) -> int:
        """This is like random pick"""
        return random.choice(self.mapp[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
