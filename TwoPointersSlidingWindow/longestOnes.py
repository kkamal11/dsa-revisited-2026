from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0
        n = len(nums)

        for i in range(n):
            zeros = 0
            for j in range(i, n):
                if nums[j] == 0:
                    zeros += 1

                if zeros <= k:
                    max_len = max(max_len, j - i + 1)
                else:
                    break

        return max_len
    
    def longestOnesOptimized(self, nums: List[int], k: int) -> int:
        max_len = 0
        l = 0
        n = len(nums)
        zeros = 0
        for r in range(n):

            if nums[r] == 0:
                zeros += 1

            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
        
        return max_len



nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
num1 = [1,1,1,0,0,0,1,1,1,1,0]
k1 = 2
sol = Solution()
print(sol.longestOnes(nums, k))
print(sol.longestOnes(num1, k1))

print(sol.longestOnesOptimized(nums, k))
print(sol.longestOnesOptimized(num1, k1))