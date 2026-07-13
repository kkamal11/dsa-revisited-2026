from typing import List


class Solution:
    def is_sequential(self, num: int) -> bool:
        prev = None
        while num:
            r = num % 10
            if prev is not None and r + 1 != prev:
                return False
            prev = r
            num //= 10
        return True

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for num in range(low, high + 1):
            if self.is_sequential(num):
                ans.append(num)
        return ans


lo = 1000
hi = 13000
sol = Solution()
print(sol.sequentialDigits(lo, hi))
