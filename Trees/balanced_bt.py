from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(r):
            if r is None:
                return 0
            
            lh = helper(r.left)
            rh = helper(r.right)

            if lh == -1 or rh == -1:
                return -1
            
            if abs(lh - rh) > 1:
                return -1

            return max(lh, rh) + 1
        
        return helper(root) != -1
