class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if n == 0:
            return ans
        if n < 0:
            x = 1 / x
            n = -n
        for i in range(n):
            ans *= x
        return ans

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1 / x
            n = -n
        ans = 1.0
        while n > 0:  # x^
            if n % 2 == 1:
                ans *= x
            x *= x
            n //= 2
        return ans

    def power(self, x, n):
        if n == 0:
            return 1.0

        if n == 1:
            return x

        if n % 2 == 0:
            return self.power(x * x, n // 2)

        return x * self.power(x, n - 1)

    def myPow(self, x, n):
        if n < 0:
            return 1.0 / self.power(x, -n)

        return self.power(x, n)


sol = Solution()
x = 2.0
n = 10
result = sol.myPow(x, n)

print(f"{x}^{n} = {result}")
