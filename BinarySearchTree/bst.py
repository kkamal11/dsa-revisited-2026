from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root is None:
            return None

        if root.val == val:
            return root
        
        if root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
    
    def searchBSTRecursive(self, root, val):

        while root:
            if root.val == val:
                return root
            if root.val > val:
                root = root.left
            else:
                root = root.right
        
        return None
        

