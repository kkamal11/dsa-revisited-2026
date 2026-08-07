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

    def reverseStr(self, s: str, k: int) -> str:

        ans = []

        count = 0
        q = deque([])
        rev = True

        for ch in s:
            q.append(ch)
            count += 1

            if count == k:
                while q:
                    if rev:
                        ans.append(q.pop())
                    else:
                        ans.append(q.popleft())
                rev = not rev
                count = 0

        while q:
            ans.append(q.pop()) if rev else ans.append(q.popleft())

        return "".join(ans)
