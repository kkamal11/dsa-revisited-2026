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

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        l1, l2 = len(list1), len(list2)
        min_idx_sum = float("inf")
        ans = []
        mapp = {}

        for i in range(l1):
            mapp[list1[i]] = i

        for j in range(l2):
            if list2[j] in mapp:
                if mapp[list2[j]] + j < min_idx_sum:
                    min_idx_sum = mapp[list2[j]] + j
                    while ans:
                        ans.pop()
                    ans.append(list2[j])
                elif min_idx_sum == mapp[list2[j]] + j:
                    ans.append(list2[j])

        return ans

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        min_idx_sum = float("inf")
        ans = []
        mapp = {s: i for i, s in enumerate(list1)}

        for j in range(len(list2)):
            s = list2[j]
            if s in mapp:
                idx = mapp[s]
                if idx + j < min_idx_sum:
                    min_idx_sum = idx + j
                    ans = [s]
                elif min_idx_sum == idx + j:
                    ans.append(s)

        return ans
