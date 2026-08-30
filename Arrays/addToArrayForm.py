from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = num.pop(0)

        for val in num:
            n = n * 10 + val

        add = n + k
        tmp = []

        while add:
            r = add % 10
            add //= 10
            tmp.append(r)

        ans = []
        while tmp:
            ans.append(tmp.pop())

        return ans

    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        ans = []
        carry = 0

        while k > 0 or carry:
            r = k % 10
            last = num.pop() if num else 0
            digit = last + r + carry

            carry = digit // 10
            digit = digit % 10

            ans.append(digit)
            k //= 10

        ans.reverse()

        return num + ans if num else ans

    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        ans = []
        carry = 0

        while k > 0 or carry:
            last = num.pop() if num else 0
            digit = last + (k % 10) + carry

            ans.append(digit % 10)
            carry = digit // 10
            k //= 10

        ans.reverse()

        return num + ans if num else ans
