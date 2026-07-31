from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if root is None:
            return ans

        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
                if node.left.left is None and node.left.right is None:
                    ans += node.left.val
            if node.right:
                q.append(node.right)

        return ans
