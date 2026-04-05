from typing import List


class Solution:
    MOD = 10**9 + 7

    def sumSubarrayMins(self, arr: List[int]) -> int:
        sum_ = 0
        n = len(arr)

        for i in range(n):
            min_ = float("inf")
            for j in range(i, n):
                min_ = min(min_, arr[j])
                sum_ += min_ % self.MOD

        return sum_ % self.MOD

    def sumSubarrayMinsOptimized(self, arr: List[int]) -> int:
        pass


sol = Solution()
arr = [11, 81, 94, 43, 3]
print(sol.sumSubarrayMins(arr))
