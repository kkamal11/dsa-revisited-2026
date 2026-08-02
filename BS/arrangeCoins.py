class Solution:
    def arrangeCoins(self, n: int) -> int:
        coins = 0
        rows = 0

        while coins <= n:
            rows += 1
            coins += rows

        return rows - 1 if coins != n else rows
