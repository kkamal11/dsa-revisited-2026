from typing import Optional


# Definition for a binary tree node.
"""
At each node, we check if it's a leaf node. 
If it is, we compare the target sum with the node's value. 
If they are equal, we return True. If not, we return False.

If the node is not a leaf, we subtract the node's value from 
the target sum and recursively check both the left and right subtrees.
The time complexity of this solution is O(n), where n is the number of nodes in the tree,
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        if root.left is None and root.right is None:
            return targetSum == root.val

        rem = targetSum - root.val
        return self.hasPathSum(root.left, rem) or self.hasPathSum(root.right, rem)
