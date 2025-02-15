#
# Complete the 'removeDuplicates' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def removeDuplicates(llist):
    # Store the reference to the head of the list
    save = llist  
    # Temporary pointer to traverse the list
    tmp = save  
    
    # Traverse the linked list
    while llist is not None:
        # Skip duplicate nodes by moving the pointer ahead
        while llist.next is not None and llist.next.data == llist.data:
            llist = llist.next  
        
        # Link the current node to the next unique node
        save.next = llist.next  
        # Move the save pointer forward
        save = save.next  
        # Move the main traversal pointer forward
        llist = llist.next  
    
    # Return the modified linked list
    return tmp