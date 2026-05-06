import copy
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

        row = len(board)
        col = len(board[0])

        board_copy = copy.deepcopy(board)

        for i in range(row):
            for j in range(col):
                live_cell = 0
                dead_cell = 0
                for dr, dc in dirs:
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < row and 0 <= nc < col:
                        if board[nr][nc] == 1:
                            live_cell += 1
                        if board[nr][nc] == 0:
                            dead_cell += 1
                if board[i][j] == 1 and live_cell < 2:
                    board_copy[i][j] = 0
                elif board[i][j] == 1 and live_cell in [2, 3]:
                    board_copy[i][j] = 1
                elif board[i][j] == 1 and live_cell > 3:
                    board_copy[i][j] = 0
                elif board[i][j] == 0 and live_cell == 3:
                    board_copy[i][j] = 1

        for i in range(row):
            for j in range(col):
                board[i][j] = board_copy[i][j]

    def gameOfLife2(self, board: List[List[int]]) -> None:
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

        row, col = len(board), len(board[0])

        for i in range(row):
            for j in range(col):
                live = 0

                for dr, dc in dirs:
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < row and 0 <= nc < col:
                        if abs(board[nr][nc]) == 1:  # original alive
                            live += 1

                if board[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = -1  # live → dead
                else:
                    if live == 3:
                        board[i][j] = 2  # dead → live

        for i in range(row):
            for j in range(col):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
