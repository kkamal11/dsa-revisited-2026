from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        Given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
        """
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                if j > i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        def reverse(L):
            left = 0
            right = len(L) - 1
            while left <= right:
                L[left], L[right] = L[right], L[left]
                left += 1
                right -= 1
            return L

        for i in range(row):
            matrix[i] = reverse(matrix[i])
