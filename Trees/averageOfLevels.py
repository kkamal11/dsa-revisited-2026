from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        q = deque([root])
        avg = []

        while q:
            s = 0
            size = len(q)

            for _ in range(size):
                node = q.popleft()
                s += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            level_avg = s / size
            avg.append(level_avg)

        return avg
