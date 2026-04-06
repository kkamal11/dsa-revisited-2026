from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            sum_ = 0
            for j in range(i,n):
                sum_ += nums[j]

                if sum_ == goal:
                    count += 1
                    
        return count

    def numSubarraysWithSumOptimised(self, nums: List[int], goal: int) -> int:
        def helper(nums, goal):
            if goal < 0:
                return 0
            count = 0
            l = 0
            sum_ = 0
            n = len(nums)
            for r in range(n):
                sum_ += nums[r]

                while sum_ > goal:
                    sum_ -= nums[l]
                    l += 1

                if sum_ <= goal:
                    count += r -l + 1
            return count
        
        return helper(nums, goal) - helper(nums, goal-1)

    def numSubarraysWithSumOptimised2(nums, goal):
        prefix_sum = 0
        count = 0
        freq = {0: 1} 

        for num in nums:
            prefix_sum += num

            if prefix_sum - goal in freq:
                count += freq[prefix_sum - goal]

            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return count
sol = Solution()
nums = [1,0,1,0,1]
goal = 2
# print(sol.numSubarraysWithSum(nums,goal))
print(sol.numSubarraysWithSumOptimised(nums,goal))