from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if (p is None and q is not None) or (p is not None and q is None):
            return False

        if p is None and q is None:
            return True
        
        if p.val != q.val:
            return False
        
        pr = p.right
        pl = p.left
        
        qr = q.right
        ql = q.left
        

        r_ans = self.isSameTree(pr, qr)
        if not r_ans:
            return False

        l_ans = self.isSameTree(pl, ql)
        if not l_ans:
            return False

        return True
        