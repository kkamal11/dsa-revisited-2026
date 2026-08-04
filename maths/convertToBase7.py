class Solution:
    def convertToBase7(self, num: int) -> str:
        digits = []
        n = abs(num)
        positive = num > 0

        while n > 0:
            rem = n % 7
            digits.append(str(rem))
            n //= 7

        ans = "".join(reversed(digits))

        return "0" if num == 0 else (ans if positive else "-" + ans)
