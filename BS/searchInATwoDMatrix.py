"""search in a matrix part 1
1. loop through row loop through col -> find if mat[i][j] == target
    O(mn)
2. Run binary search along row/col and see if target is found
    O(m log n)
3. Flatten matrix -> Run binary searcg
   Instead of flattening the matrix and storing the matrix itself can be treated as flattened array
    -> If rows are sorted
    -> lo = 0, hi = mn-1
    -> mid = (lo+hi)//2   row = mid /n  col = mid % n
"""

"""
search in a matrix part 2
individual rows and cols are sorted
1. use two loops and look for target O(mn)
2. run binary search on each row mlogn
3. starting at last cell of first rwo we see its sorted in L saped
    O(m+n)
"""


def searchInATwoDMatrix2(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    row = 0
    col = n - 1
    while row < m and col >= 0:
        if matrix[row][col] == target:
            return True
        if matrix[row][col] > target:
            col = col - 1
        else:
            row = row + 1
    return False
