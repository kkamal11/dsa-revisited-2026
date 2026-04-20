from collections import deque


class Solution:
    def rottenOranges(self, grid):
        time = 0
        row = len(grid)
        col = len(grid[0])

        q = deque()
        fresh = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q and fresh > 0:
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = dr + r, dc + c
                    if nr >= 0 and nr < row and nc >= 0 and nc < col:
                        if grid[nr][nc] == 1:
                            fresh -= 1
                            q.append((nr, nc))
                            grid[nr][nc] = 2
            time += 1

        return time if fresh == 0 else -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
sol = Solution()
print(sol.rottenOranges(grid))
