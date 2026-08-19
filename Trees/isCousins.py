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


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        q = deque([(root, root)])

        while q:
            size = len(q)
            x_parent = None
            y_parent = None
            for _ in range(size):
                node, parent = q.popleft()

                if node.val == x:
                    x_parent = parent.val
                if node.val == y:
                    y_parent = parent.val

                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))

                if x_parent is not None and y_parent is not None:
                    return x_parent != y_parent

        return False
