#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def sortedInsert(llist, data):
    # Create a new node with the given data
    node = DoublyLinkedListNode(data)
    
    # If the list is empty, return the new node
    if llist is None:
        return node 
    
    save = llist 
    
    # Traverse the list to find the correct insertion point
    while llist is not None and llist.data < data:
        pre = llist
        llist = llist.next
    
    # Insert at the end
    if llist is None:
        pre.next = node
        node.prev = pre
        return save
    
    # Insert at the head
    if llist.prev is None:
        llist.prev = node
        node.next = llist
        return node
    
    # Insert in the middle
    node.next = llist
    node.prev = llist.prev
    llist.prev.next = node
    llist.prev = node
    
    return save