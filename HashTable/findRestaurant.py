from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        l1, l2 = len(list1), len(list2)
        min_idx_sum = float("inf")
        ans = []

        for i in range(l1):
            for j in range(l2):
                if list1[i] == list2[j]:
                    min_idx_sum = min(min_idx_sum, i + j)

        for i in range(l1):
            for j in range(l2):
                if list1[i] == list2[j] and i + j == min_idx_sum:
                    ans.append(list1[i])

        return ans
