from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        ans_mat = [[0] * cols for _ in range(rows)]
        visited = [[0] * cols for _ in range(rows)]

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        q = deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    visited[i][j] = 1

        while q:
            r, c, dist = q.popleft()
            ans_mat[r][c] = dist

            for dr, dc in dirs:
                drow = r + dr
                dcol = c + dc

                if 0 <= drow < rows and 0 <= dcol < cols:
                    if visited[drow][dcol] != 1:
                        visited[drow][dcol] = 1
                        q.append((drow, dcol, dist + 1))

        return ans_mat
