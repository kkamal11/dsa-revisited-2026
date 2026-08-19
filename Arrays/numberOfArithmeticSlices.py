from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            cur_seq_len = 1
            last = nums[i]
            diff = None

            for j in range(i + 1, n):
                if diff is None:
                    diff = nums[j] - last
                elif nums[j] - last != diff:
                    break
                cur_seq_len += 1
                if cur_seq_len >= 3:
                    count += 1
                last = nums[j]

        return count


sol = Solution()
nums = [1, 2, 3, 4]
print(sol.numberOfArithmeticSlices(nums))  # Output: 3
