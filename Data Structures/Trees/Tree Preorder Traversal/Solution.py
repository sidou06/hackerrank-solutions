"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    # Write your code here

    if root != None:
        print(root.info, end=' ')  # Print the current node's value with a space
        preOrder(root.left)  # Recursively traverse the left subtree
        preOrder(root.right)  # Recursively traverse the right subtree