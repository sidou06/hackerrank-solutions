"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def inOrder(root):
    # Write your code here
    
    if root != None:
        inOrder(root.left)  # Recursively traverse the left subtree
        print(root.info, end=' ')  # Print the current node's value with a space
        inOrder(root.right)  # Recursively traverse the right subtree