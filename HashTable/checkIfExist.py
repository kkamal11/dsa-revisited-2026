from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)

        for i in range(n):
            for j in range(n):
                if i != j and arr[i] == 2 * arr[j]:
                    return True

        return False

    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()

        for num in arr:
            if num * 2 in seen:
                return True
            if num % 2 == 0 and num // 2 in seen:
                return True
            seen.add(num)

        return False
