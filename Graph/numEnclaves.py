from collections import deque
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (
                    i == 0 or i == rows - 1 or j == 0 or j == cols - 1
                ):
                    grid[i][j] = -1
                    q.append((i, j))

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                drow, dcol = dr + r, dc + c

                if 0 <= drow < rows and 0 <= dcol < cols:
                    if grid[drow][dcol] == 1:
                        grid[drow][dcol] = -1
                        q.append((drow, dcol))

        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count += 1

        return count


sol = Solution()
grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
print(sol.numEnclaves(grid))
print(sol.numEnclavesDFS(grid))
