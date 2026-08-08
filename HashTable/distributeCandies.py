from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        map_types = {}

        for ty in candyType:
            map_types[ty] = map_types.get(ty, 0) + 1

        n = len(candyType) // 2
        type_count = 0

        for ty in map_types:
            n -= 1
            type_count += 1
            if n == 0:
                break

        return type_count
