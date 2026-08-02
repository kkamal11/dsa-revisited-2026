class Solution:
    def arrangeCoins1(self, n: int) -> int:
        coins = 0
        rows = 0

        while coins <= n:
            rows += 1
            coins += rows

        return rows - 1 if coins != n else rows

    def arrangeCoins(self, n: int) -> int:
        lo = 0
        hi = n

        while lo <= hi:
            mid = (lo + hi) // 2
            coins = mid * (mid + 1) // 2

            if coins == n:
                return mid
            elif coins < n:
                lo = mid + 1
            else:
                hi = mid - 1

        return hi


sol = Solution()
n = 8
print(sol.arrangeCoins1(n), sol.arrangeCoins(n))
