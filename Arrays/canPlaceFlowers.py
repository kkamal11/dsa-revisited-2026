from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)

        if n == 0:
            return True

        if m == 1:
            if n > 1:
                return False
            if n == 1 and flowerbed[0] == 1:
                return False
            return True

        for i in range(m):
            if flowerbed[i] == 0:
                if i == 0 and flowerbed[i + 1] == 0:
                    n -= 1
                    flowerbed[i] = 1
                elif i == m - 1 and flowerbed[i - 1] == 0:
                    n -= 1
                    flowerbed[i] = 1
                elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    n -= 1
                    flowerbed[i] = 1

            if n == 0:
                return True

        return n == 0
