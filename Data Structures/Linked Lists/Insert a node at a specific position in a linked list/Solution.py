#
# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtPosition(llist, data, position):
    # Create a new node with the given data
    nv = SinglyLinkedListNode(data)  

    # If inserting at the head, update the new head and return it
    if position == 0:
        nv.next = llist  
        return nv  

    # Traverse to the node before the desired position
    prec = llist  
    for i in range(position - 1):
        prec = prec.next  

    # Save the reference to the next node
    suiv = prec.next  

    # Insert the new node between the previous and next nodes
    prec.next = nv  
    nv.next = suiv  

    # Return the head of the linked list
    return llist