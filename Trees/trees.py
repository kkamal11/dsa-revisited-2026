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