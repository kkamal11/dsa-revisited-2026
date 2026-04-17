from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def insertIntoBSTRecursion(self, root, val):
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        
        return root
    
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        tmp = root
        
        if tmp is None:
            return TreeNode(val)

        while tmp:
            if tmp.val < val:
                if tmp.right:
                    tmp = tmp.right
                else:
                    tmp.right = TreeNode(val)
                    break
            else:
                if tmp.left:
                    tmp = tmp.left
                else:
                    tmp.left = TreeNode(val)
                    break
        return root