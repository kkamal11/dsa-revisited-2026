from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        count = 0

        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                count += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return count

    def countNodesDfs(self, root: Optional[TreeNode]):
        count = 0
        visited = set()
        if root is None:
            return count

        def dfs(root):
            if root is None or root in visited:
                return

            nonlocal count
            count += 1
            visited.add(root)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

        dfs(root)
        return count


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def left_height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        def right_height(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h

        if not root:
            return 0

        lh = left_height(root)
        rh = right_height(root)

        if lh == rh:
            return (1 << lh) - 1  # 2^h - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
