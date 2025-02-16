# Enter your code here. Read input from STDIN. Print output to STDOUT

'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree, which contains info as data, left, right
'''

def height(root):
    # Base case: If the tree is empty, return 0
    if root == None:
        return 0
    
    # If the node is a leaf node (no children), return 0
    elif root.right == root.left == None:
        return 0
    
    # Recursively compute the height of left and right subtrees and return the maximum + 1
    else:
        return 1 + max(height(root.left), height(root.right))