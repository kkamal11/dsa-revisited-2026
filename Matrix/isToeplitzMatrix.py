from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                ni, nj = i + 1, j + 1
                if ni < rows and nj < cols and matrix[i][j] != matrix[ni][nj]:
                    return False

        return True
