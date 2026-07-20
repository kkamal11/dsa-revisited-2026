from typing import List


class Solution:
    def shift_right(self, arr: List[int], k) -> List[int]:
        return arr[-k:] + arr[: len(arr) - k]

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        total = rows * cols
        k %= total

        ans = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                old = i * cols + j
                new = (old + k) % total

                new_row = new // cols
                new_col = new % cols

                ans[new_row][new_col] = grid[i][j]

        return ans

    def print_matries(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                print(grid[i][j], end=" ")
            print()


sol = Solution()
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sol.print_matries(grid)
print(sol.shiftGrid(grid, 1))
