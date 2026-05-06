from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []


"""
      1
    1 2 3
  1 2 3 4 5
   
"""


class Solution:
    def removeChildrenAtLevel(self, root, targetLevel):
        if not root:
            return None

        if targetLevel == 1:
            return None

        q = deque([root])
        current_level = 1

        while q:
            size = len(q)

            if current_level == targetLevel - 1:
                for _ in range(size):
                    node = q.popleft()

                    new_children = []
                    for child in node.children:
                        new_children.extend(child.children)

                    node.children = new_children
                break

            for _ in range(size):
                node = q.popleft()
                for child in node.children:
                    q.append(child)

            current_level += 1

        return root
