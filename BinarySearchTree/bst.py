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
    
    def searchMaxInBST(self, root):
        max_ = float('-inf')

        while root:
            max_ = max(max_, root.val)
            root = root.right
        
        return max_

    def searchMinInBST(self, root):
        min_ = float('inf')

        while root:
            min_ = min(min_, root.val)
            root = root.left
        
        return min_
        

