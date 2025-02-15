#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts INTEGER_DOUBLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#

def reverse(llist):
    # If the list is empty or has only one node, return it as is
    if llist == None or llist.next == None:
        return llist 

    while llist != None:
        cp = llist.next  # Store the next node temporarily
        llist.next = llist.prev  # Swap the next and previous pointers
        llist.prev = cp  # Assign the stored next node to prev
        save = llist  # Keep track of the new head of the reversed list
        llist = cp  # Move to the next node in the original order

    return save  # Return the new head of the reversed list