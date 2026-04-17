from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []
        left = False

        if root is None:
            return res
        
        q.append(root)
        while q:
            size = len(q)
            sub_list = []
            left = not left
            for _ in range(size):
                node = q.popleft()
                sub_list.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if left:
                res.append(sub_list)
            else:
                res.append(list(reversed(sub_list)))
            
        return res