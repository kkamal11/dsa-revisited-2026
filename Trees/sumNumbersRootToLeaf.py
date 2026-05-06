from typing import Optional
from collections import deque


# Definition for a binary tree node.
"""
Given a binary tree containing digits from 0-9 only, 
each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the
 number 123.


At each node:
current_number = previous_number * 10 + node.val
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, root.val)])

        final_num = []
        while q:
            for _ in range(len(q)):
                node, n = q.popleft()

                if node.left is None and node.right is None:
                    final_num.append(n)

                if node.left:
                    n1 = 10 * n + node.left.val
                    q.append((node.left, n1))

                if node.right:
                    n2 = 10 * n + node.right.val
                    q.append((node.right, n2))

        return sum(final_num)


class Solution:
    def sumNumbers(self, root):
        def dfs(node, curr):
            if not node:
                return 0

            curr = curr * 10 + node.val

            if not node.left and not node.right:
                return curr

            return dfs(node.left, curr) + dfs(node.right, curr)

        return dfs(root, 0)
