# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        q = deque([(root, root)])

        levels = []

        while q:
            size = len(q)
            curr_level = set()
            for _ in range(size):
                node, parent = q.popleft()
                curr_level.add(node.val)
                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))
            levels.append(curr_level)
        print(levels)

        return False
