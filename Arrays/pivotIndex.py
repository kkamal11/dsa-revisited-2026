from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        n = len(nums)
        left_sum = [0] * n
        right_sum = [0] * n

        for i in range(1, n):
            left_sum[i] = left_sum[i - 1] + nums[i - 1]
    
        for i in range(n - 1, -1, -1):
            if i != n - 1:
                right_sum[i] = right_sum[i + 1] + nums[i + 1]
        
        for i in range(n):
            ls = left_sum[i]
            rs = right_sum[i]
            if ls == rs:
                return i
        
        return -1
            
        