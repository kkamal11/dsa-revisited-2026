class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        count = 0
        primes = [1] * (n + 1)
        for i in range(2, n):
            if primes[i] == 1:
                count += 1
                for j in range(2 * i, n + 1, i):
                    primes[j] = 0
        return count

    def countPrimesOptimized(self, n: int) -> int:
        """
        TC - nlog (log n)
        """
        if n < 2:
            return 0
        count = 0
        primes = [1] * (n + 1)
        i = 2
        while i * i <= n:
            if primes[i] == 1:
                count += 1
                for j in range(i * i, n + 1, i):
                    primes[j] = 0
            i += 1
        return count


sol = Solution()
n = 18
print(sol.countPrimes(n))
