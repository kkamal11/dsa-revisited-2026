from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float("-inf")

        n = len(nums)

        for i in range(n):
            s = 0
            count = 0
            for j in range(i, n):
                s += nums[j]
                count += 1
                if count == k:
                    max_avg = max(max_avg, s / k)

        return max_avg

    def findMaxAverage2(self, nums: List[int], k: int) -> float:
        window_sum = 0
        max_avg = float("-inf")

        i, j, n = 0, 0, len(nums)

        while j < n:
            window_sum += nums[j]
            if (j - i + 1) == k:
                max_avg = max(max_avg, window_sum / k)
            while (j - i + 1) > k:
                window_sum -= nums[i]
                i += 1
                max_avg = max(max_avg, window_sum / k)
            j += 1

        return max_avg

    def findMaxAverage3(self, nums: List[int], k: int) -> float:
        window_sum = 0
        max_avg = float("-inf")

        i, j, n = 0, 0, len(nums)

        while j < n:
            window_sum += nums[j]

            if (j - i + 1) == k:
                max_avg = max(max_avg, window_sum / k)
                window_sum -= nums[i]
                i += 1

            j += 1

        return max_avg


sol = Solution()
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(sol.findMaxAverage(nums, k))
print(sol.findMaxAverage2(nums, k))
