from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)

        moves = float("inf")

        for i in range(n):
            curr = 0
            for j in range(n):
                if i != j:
                    curr += abs(nums[i] - nums[j])
            moves = min(moves, curr)

        return moves
