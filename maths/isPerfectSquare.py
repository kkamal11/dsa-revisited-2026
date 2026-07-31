class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1, num + 1):
            if i * i == num:
                return True
        return False

    def isPerfectSquare(self, num: int) -> bool:
        lo = 1
        hi = num + 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid == num:
                return True

            if mid * mid < num:
                lo = mid + 1
            if mid * mid > num:
                hi = mid - 1

        return False
