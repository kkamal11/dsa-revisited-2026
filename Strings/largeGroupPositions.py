from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []

        last = None
        startIdx = 0

        for endIdx, ch in enumerate(s):
            if last != ch:
                if endIdx - startIdx > 2:
                    ans.append([startIdx, endIdx - 1])
                last = ch
                startIdx = endIdx

        if endIdx - startIdx + 1 >= 3:
            ans.append([startIdx, endIdx])

        return ans
