#Inorder Traversal
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Creating a simple binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Traversing the binary tree
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.data, end=" ")
        inorder_traversal(node.right)


print("Inorder Traversal:")
inorder_traversal(root)
print("\n")


