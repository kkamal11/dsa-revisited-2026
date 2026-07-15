class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_odd = n * n
        sum_even = n * (n + 1)

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        return gcd(sum_odd, sum_even)
