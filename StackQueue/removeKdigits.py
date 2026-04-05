from typing import List


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for ch in num:
            while stack and stack[-1] > ch and k > 0:
                stack.pop()
                k -= 1

            if not stack and ch == "0":
                continue

            stack.append(ch)

        while k > 0 and stack:
            stack.pop()
            k -= 1

        return "".join(stack).lstrip("0") if stack else "0"


num1 = "1432219"
k1 = 3
num2 = "10200"
k2 = 1
num3 = "10"
k3 = 2
num4 = "9"
k4 = 1
sol = Solution()
print(sol.removeKdigits(num1, k1))
print(sol.removeKdigits(num2, k2))
print(sol.removeKdigits(num3, k3))
print(sol.removeKdigits(num4, k4))
