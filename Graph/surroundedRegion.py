from typing import List
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        rows = len(board)
        cols = len(board[0])

        marked = [[0] * cols for _ in range(rows)]

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (
                    i == 0 or i == rows - 1 or j == 0 or j == cols - 1
                ):
                    marked[i][j] = -1
                    q.append((i, j))

        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                drow = dr + r
                dcol = dc + c
                if 0 <= drow < rows and 0 <= dcol < cols:
                    if board[drow][dcol] == "O" and marked[drow][dcol] == 0:
                        marked[drow][dcol] = -1
                        q.append((drow, dcol))

        for i in range(rows):
            for j in range(cols):
                if marked[i][j] == 0 and board[i][j] == "O":
                    board[i][j] = "X"

        return board
