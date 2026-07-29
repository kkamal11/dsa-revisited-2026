from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insert_idx = 0
        n = len(nums)

        for i in range(n):
            if nums[i] != val:
                nums[insert_idx] = nums[i]
                insert_idx += 1

        return insert_idx


sol = Solution()
nums = [3, 2, 2, 3]
val = 3
k = sol.removeElement(nums, val)
print(k)
