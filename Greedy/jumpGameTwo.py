from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        max_far = 0
        n = len(nums)
        step = 0

        for i in range(n):
            curr_far = i + nums[i]
            max_far = max(max_far, curr_far)
            if i > max_far:
                return -1

            if i == max_far:
                step += 1
                
        return step
            



sol = Solution()
nums = [2,3,1,1,4]
print(sol.jump(nums))

nums = [2,3,0,1,4]
print(sol.jump(nums))