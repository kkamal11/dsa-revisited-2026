from collections import deque


class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        ans = []

        count = 0
        tmp = ""
        rev = True

        for ch in s:
            if rev:
                tmp = ch + tmp
            else:
                tmp += ch

            count += 1

            if count == k:
                ans.append(tmp)
                tmp = ""
                rev = not rev
                count = 0

        if tmp:
            ans.append(tmp)

        return "".join(ans)
