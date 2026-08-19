from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = [0] * n
        insert_idx = 0

        for num in nums:
            if num % 2 == 0:
                ans[insert_idx] = num
                insert_idx += 1

        for num in nums:
            if num % 2 == 1:
                ans[insert_idx] = num
                insert_idx += 1

        return ans
