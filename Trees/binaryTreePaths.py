from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        q = deque([[root, str(root.val)]])
        ans = []

        while q:
            node, path = q.popleft()

            if not node.left and not node.right:
                ans.append(path)

            if node.left:
                q.append([node.left, path + "->" + str(node.left.val)])
            if node.right:
                q.append([node.right, path + "->" + str(node.right.val)])

        return ans

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def dfs(node, path):
            if not node:
                return

            path += str(node.val)

            if not node.left and not node.right:
                ans.append(path)
                return

            path += "->"
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return ans
