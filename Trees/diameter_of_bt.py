from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Ways to find diameter of binary tree:
    1. For each node, find the longest path through that node and update the diameter.
       This can be done by finding the maximum depth of left and right subtrees for each node.
       Time complexity: O(n^2) in worst case (skewed tree), O(n log n) in average case (balanced tree).
       Space complexity: O(h) where h is the height of the tree due to recursion stack.
    """

    def max_depth(self, root):
        if root is None:
            return 0

        lh = self.max_depth(root.left)
        rh = self.max_depth(root.right)

        return 1 + max(lh, rh)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")

        def helper(r):
            if r is None:
                return 0

            lh = self.max_depth(r.left)
            rh = self.max_depth(r.right)

            nonlocal ans
            ans = max(ans, lh + rh)

            self.diameterOfBinaryTree(r.left)
            self.diameterOfBinaryTree(r.right)

        helper(root)

        return ans

    def diameterOfBinaryTre2e(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            if not node:
                return 0

            lh = dfs(node.left)
            rh = dfs(node.right)

            ans = max(ans, lh + rh)

            return 1 + max(lh, rh)

        dfs(root)
        return ans
