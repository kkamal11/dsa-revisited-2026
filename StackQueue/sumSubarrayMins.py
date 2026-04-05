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
        MOD = 10**9 + 7
        n = len(arr)

        stack = []
        left = [0] * n
        right = [0] * n

        for i in range(n):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                count += stack.pop()[1]
            left[i] = count
            stack.append((arr[i], count))

        stack.clear()

        for i in range(n - 1, -1, -1):
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                count += stack.pop()[1]
            right[i] = count
            stack.append((arr[i], count))

        res = 0
        for i in range(n):
            res += arr[i] * left[i] * right[i]
            res %= MOD

        return res


sol = Solution()
arr = [11, 81, 94, 43, 3]
print(sol.sumSubarrayMins(arr))
