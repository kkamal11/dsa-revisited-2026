from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}

        for num in arr:
            d[num] = d.get(num, 0) + 1

        seen = set()
        for key in d:
            if d[key] in seen:
                return False
            seen.add(d[key])

        return True
