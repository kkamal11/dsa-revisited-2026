from collections import deque

class Node:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.result = []

    def preorder(self, root):
        if root is None:
            return
        print(root.val, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)
    
    def preorder_list1(self, root):
        if root is None:
            return
        self.result.append(root.val)
        self.preorder_list1(root.left)
        self.preorder_list1(root.right)    

        return self.result
    
    def preorder_list(self, root):
        result = []

        def pre(node):
            if node is None:
                return 
            result.append(node.val)
            pre(node.left)
            pre(node.right)

        pre(root)
        return result

    def postorder(self, root):
        if root is None:
            return
        
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val, end=" ")
    

    def inorderTraversal(self, root):
        result = []
        
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)

        inorder(root)
        return result
    

    def inorderIterative(self, root):
        result = []
        stack = []
        current = root

        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            result.append(current.val)
            current = current.right
        
        return result
    
    def levelOrder(self, root):
        q = deque()
        result = []

        if root is None:
            return result

        q.append(root)

        while q:
            level = len(q)
            sub_list = []
            for i in range(level):
                r = q.popleft()
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
                
                sub_list.append(r.val)
            
            result.append(sub_list)

        return result

root = Node(1)
left = Node(2)
right =Node(3)
left_left = Node(4)
left_right = Node(5)
root.left = left
root.right = right
left.left = left_left
left.right = left_right


tree = Tree()
tree.preorder(root)
print(tree.preorder_list(root))
print(tree.preorder_list1(root))
tree.postorder(root)