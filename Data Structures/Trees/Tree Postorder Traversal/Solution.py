"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def postOrder(root):
    # Write your code here

    if root != None:  
        postOrder(root.left)  # Recursively traverse the left subtree
        postOrder(root.right)  # Recursively traverse the right subtree
        print(root.info, end=' ')  # Print the current node's value with a space