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
