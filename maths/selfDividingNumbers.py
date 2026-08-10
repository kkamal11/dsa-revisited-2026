from typing import List


class Solution:
    def digits_divide(self, num: int) -> bool:
        n = num
        while n > 0:
            r = n % 10
            if r == 0 or num % r != 0:
                return False
            n //= 10
        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left, right + 1):
            if self.digits_divide(num):
                ans.append(num)

        return ans
