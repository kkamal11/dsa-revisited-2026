from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def topView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # Dictionary to store the first node at each horizontal distance
        top_view_map = {}
        # Queue for level order traversal (node, horizontal distance)
        queue = deque([(root, 0)])
        
        while queue:
            node, hd = queue.popleft()
            
            # If this horizontal distance is not already in the map, add it
            if hd not in top_view_map:
                top_view_map[hd] = node.val
            
            # Add left and right children to the queue with updated horizontal distances
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        
        # Extract the values from the map in sorted order of horizontal distance
        return [top_view_map[hd] for hd in sorted(top_view_map.keys())]