from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node, leaves):
        if not node:
            return

        if not node.left and not node.right:
            leaves.append(node.val)
            return

        self.dfs(node.left, leaves)
        self.dfs(node.right, leaves)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        l1 = []
        l2 = []
        self.dfs(root1, l1)
        self.dfs(root2, l2)

        return l1 == l2
