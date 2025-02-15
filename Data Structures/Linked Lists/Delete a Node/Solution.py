#
# Complete the 'deleteNode' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def deleteNode(llist, position):
    # If deleting the head node, return the next node as the new head
    if position == 0:
        return llist.next  

    # Traverse to the node before the one to be deleted
    cu = llist
    for i in range(position - 1):
        cu = cu.next  

    # Store the node to be deleted
    dell = cu.next  

    # Link the current node to the next of the node to be deleted
    cu.next = dell.next  

    # Return the head of the linked list
    return llist