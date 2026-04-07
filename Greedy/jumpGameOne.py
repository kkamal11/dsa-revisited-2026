from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_idx = 0
        n = len(nums)

        for i in range(n):
            
            if i > max_idx:
                return False
            
            curr_step = nums[i]
            max_idx = max(max_idx, i + curr_step)

        return True
    
sol = Solution()
nums = [2,3,1,1,4]
print(sol.canJump(nums))

nums = [2,1,1,0,4]
print(sol.canJump(nums))