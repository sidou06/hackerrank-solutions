#
# Complete the 'getNode' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER positionFromTail
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def getNode(llist, positionFromTail):
    # Initialize a list to store node data
    nodes = []  
    
    # Traverse the linked list and store data in the list
    while llist is not None:
        nodes.append(llist.data)  
        llist = llist.next  
    
    # Return the value at the specified position from the tail
    return nodes[-positionFromTail - 1] 