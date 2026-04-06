from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        freq = {0:1}
        p_sum = 0

        for num in nums:
            p_sum += (num % 2)
            if p_sum - k in freq:
                count += freq[p_sum-k]
            freq[p_sum] = freq.get(p_sum, 0) + 1
        return count

sol = Solution()
nums = [1,1,2,1,1]
k = 3
print(sol.numberOfSubarrays(nums, k))