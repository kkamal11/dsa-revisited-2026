class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)
        i, j = m - 1, n - 1
        carry = 0

        ans = []

        while i >= 0 or j >= 0 or carry != 0:

            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            total = n1 + n2 + carry

            carry = total // 10

            ans.append(str(total % 10))

            i -= 1
            j -= 1

        return "".join(reversed(ans))
