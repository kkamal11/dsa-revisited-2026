from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = []

        count = 0
        for i in range(len(nums)):
            if not ans:
                ans.append(nums[i])
                count += 1
            elif ans[-1] == nums[i] and count < 2:
                ans.append(nums[i])
                count += 1
            elif ans[-1] != nums[i]:
                ans.append(nums[i])
                count = 1

        for i in range(len(ans)):
            nums[i] = ans[i]

        return len(ans)

    def removeDuplicates2(self, nums):
        if len(nums) <= 2:
            return len(nums)

        k = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k
