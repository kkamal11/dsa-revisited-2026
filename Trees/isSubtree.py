from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        seen = set()
        q = deque([root])

        while q:
            node = q.popleft()
            seen.add(node)
            if subRoot in seen:
                return True

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return False
