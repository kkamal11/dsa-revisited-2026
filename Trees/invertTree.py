# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Time Complexity: O(n) where n is the number of nodes in the tree. We visit each node exactly once.
        Space Complexity: O(h) where h is the height of the tree. In the worst
        case (a completely unbalanced tree), the height of the tree is n, so the space complexity is O(n).
        """
        if root is None:
            return root
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def invertTree(root):
        """
        Time Complexity: O(n) where n is the number of nodes in the tree. We visit each node exactly once.
        Space Complexity: O(n) in the worst case (a completely unbalanced tree), the
        """
        if not root:
            return None

        q = deque([root])

        while q:
            node = q.popleft()

            node.left, node.right = node.right, node.left

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return root
