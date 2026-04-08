from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
    
        n = len(nums)
        jumps = 0
        left = 0
        right = 0

        while right < n-1:
            farthest = 0
            for j in range(left, right+1):
                farthest = max(farthest, j+ nums[j])
            left = right + 1
            right = farthest
            jumps += 1

        return jumps
        
    def jump2(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        curr_end = 0   # end of current jump range
        max_reach = 0  # farthest index we can reach while scanning this range

        # We only need to process until n-2, because once we can reach last index,
        # we stop. No need to jump from the last index itself.
        for i in range(n - 1):
            max_reach = max(max_reach, i + nums[i])

            # Time to take one jump: we finished scanning current range.
            if i == curr_end:
                jumps += 1
                curr_end = max_reach

                # Optimization: if this jump can reach/past last index, done.
                if curr_end >= n - 1:
                    break

        return jumps



sol = Solution()
nums = [2,3,4,1,0,1]
print(sol.jump(nums))

nums = [2,3,0,1,0,1]
print(sol.jump2(nums))