from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_row = {i: set() for i in range(10)}
        seen_col = {i: set() for i in range(10)}
        seen_grid = {i: set() for i in range(10)}

        row = len(board)
        col = len(board[0])

        for i in range(row):
            for j in range(col):
                val = board[i][j]
                grid_id = (i // 3) * 3 + (j // 3)
                if val == ".":
                    continue
                if val in seen_row[i] or val in seen_col[j]:
                    return False
                if val in seen_grid[grid_id]:
                    return False

                seen_grid[grid_id].add(val)
                seen_row[i].add(val)
                seen_col[j].add(val)

        return True
