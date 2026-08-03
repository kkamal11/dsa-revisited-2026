class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum_ = 0

        for i in range(1, num):
            if num % i == 0:
                sum_ += i

        return num == sum_

    """
    Optimal Approach:
    Divisors occur in pairs: if i divides num, then num // i is also a divisor.
    Iterate only up to √num and add both divisors whenever a factor is found.
    If both divisors are the same (i == num // i), add it only once.
    If the sum of all proper divisors equals num, return True; otherwise, return False.
    
    """

    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        total = 1
        i = 2

        while i * i <= num:
            if num % i == 0:
                total += i
                if i != num // i:
                    total += num // i
            i += 1

        return num == total
