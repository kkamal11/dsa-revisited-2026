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

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []

        s = "123456789"

        low_len = len(str(low))
        high_len = len(str(high))

        for length in range(low_len, high_len + 1):
            for start in range(10 - length):
                num = int(s[start : start + length])

                if low <= num <= high:
                    ans.append(num)

        return ans


"""
There are only 36 possible sequential digit numbers:
2 digits: 12 23 34 45 56 67 78 89          (8)
3 digits: 123 234 345 456 567 678 789      (7)
4 digits: 1234 ... 6789                    (6)
5 digits: 12345 ... 56789                  (5)
6 digits: 123456 ... 456789                (4)
7 digits: 1234567 ... 3456789              (3)
8 digits: 12345678 23456789                (2)
9 digits: 123456789                        (1)

Total = 8+7+6+5+4+3+2+1 = 36

"""

lo = 1000
hi = 13000
sol = Solution()
print(sol.sequentialDigits(lo, hi))
