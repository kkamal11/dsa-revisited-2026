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

    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)

        moves = float("inf")

        for i in range(n):
            curr = 0
            for j in range(n):
                if i != j:
                    curr += abs(nums[i] - nums[j])
                    if curr > moves:
                        break
            moves = min(moves, curr)

        return moves

    """
    Observation: The optimal solution is to find the median of the array and calculate the sum of absolute differences from the median.
    This is because the median minimizes the sum of absolute deviations.
    """

    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)

        moves = 0
        nums.sort()

        median = nums[n // 2]

        for i in range(n):
            moves += abs(median - nums[i])

        return moves
