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
