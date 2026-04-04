class Solution:
    MOD = 10**9 + 7

    def power(self, x, n):
        if n == 0:
            return 1
        ans = 1
        if n < 0:
            x = 1 / x
            n = -n
        while n > 0:
            if n % 2 == 1:
                ans = ans * x
            x = x * x
            n = n // 2
        return ans

    def countGoodNumbers(self, n: int) -> int:
        even_pos_count = (n + 1) // 2
        odd_pos_count = n // 2
        return self.power(5, even_pos_count) * self.power(4, odd_pos_count) % self.MOD


# even_indices = [0,2,4,6,8] 5 choices
# odd_indices = [2,3,5,7] 4 choices
sol = Solution()
n = 50
print(sol.countGoodNumbers(n))
