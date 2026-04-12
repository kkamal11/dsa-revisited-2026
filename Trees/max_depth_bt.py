from collections import deque

class Node:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None


def max_depth(root:Node):
    q = deque()
    depth = 0

    if root is None:
        return depth
    
    q.append(root)

    while q:
        level_size = len(q)
        depth += 1
        for _ in range(level_size):
            r = q.popleft()

            if r.left:
                q.append(r.left)
            if r.right:
                q.append(r.right)

    return depth


def max_depth_recurive(root):
    if root is None:
        return 0
    
    lh = max_depth_recurive(root.left)
    rh = max_depth_recurive(root.right)

    return 1 + max(lh, rh)