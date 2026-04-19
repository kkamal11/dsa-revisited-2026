from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)-1
        def helper(n):
            if n == 0:
                return nums[0]
            if n < 0:
                return 0
            
            pick = nums[n] + helper(n-2)
            n_pick = helper(n-1)

            return max(pick, n_pick)
        
        return helper(n)


