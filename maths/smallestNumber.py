class Solution:
    def digit_product(self, num):
        if num == 0:
            return 0

        prod = 1
        while num > 0:
            r = num % 10
            prod *= r
            num //= 10

        return prod

    def smallestNumber(self, n: int, t: int) -> int:
        div = self.digit_product(n) % t

        while div:
            n += 1
            div = self.digit_product(n) % t

        return n
