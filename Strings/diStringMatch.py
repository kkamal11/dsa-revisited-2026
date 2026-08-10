from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        left, right = 0, n
        perm = []

        for ch in s:
            if ch == "I":
                perm.append(left)
                left += 1
            else:
                perm.append(right)
                right -= 1

        perm.append(left)

        return perm
