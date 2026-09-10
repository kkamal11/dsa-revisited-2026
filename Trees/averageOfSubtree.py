from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def average_value_sub_tree(self, root: TreeNode) -> int:
        q = deque([root])
        node_value_sum = 0
        node_count = 0

        while q:
            node = q.popleft()
            node_value_sum += node.val
            node_count += 1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return int(node_value_sum / node_count)

    def averageOfSubtree(self, root: TreeNode) -> int:

        q = deque([root])
        count = 0

        while q:
            node = q.popleft()
            if node.val == self.average_value_sub_tree(node):
                count += 1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return count

    def averageOfSubtreeDFS(self, root: TreeNode) -> int:
        count = 0

        def dfs(node):
            nonlocal count
            if not node:
                return (0, 0)  # sum, count

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            if node.val == total_sum // total_count:
                count += 1

            return (total_sum, total_count)

        dfs(root)
        return count
