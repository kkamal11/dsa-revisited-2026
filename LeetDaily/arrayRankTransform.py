from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums = sorted(arr)
        rank = 1
        rank_arr = dict()
        last = None
        for num in nums:
            if rank_arr and last != num:
                rank += 1
                rank_arr[num] = rank
            # else:
            #     rank_arr[num] = rank
            last = num

        ans = []
        for num in arr:
            ans.append(rank_arr[num])

        return ans

    def arrayRankTransform2(self, arr: List[int]) -> List[int]:
        nums = sorted(arr)
        rank = 0
        rank_map = dict()

        for num in nums:
            if num not in rank_map:
                rank += 1
                rank_map[num] = rank

        return [rank_map[num] for num in arr]
