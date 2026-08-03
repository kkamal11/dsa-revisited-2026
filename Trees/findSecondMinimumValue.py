from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        sec_min = -1
        mini = float("inf")
        q = deque([root])

        while q:
            node = q.popleft()
            val = node.val
            if val < mini:
                sec_min = mini
                mini = val
            elif val != mini and val < sec_min:
                sec_min = val

            if node.right and node.left:
                q.append(node.right)
                q.append(node.left)

        return -1 if sec_min == float("inf") else sec_min
