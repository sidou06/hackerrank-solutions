#
# Complete the 'reverse' function below.
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

def reverse(llist):
    # Store nodes in a list
    nodes = []
    while llist is not None:
        nodes.append(llist) 
        llist = llist.next 

    # Initialize the new head
    res = None 
    if len(nodes) > 0:
        res = nodes[-1]  
        save = res  

    # Reverse the pointers
    for i in range(len(nodes) - 2, -1, -1):
        res.next = nodes[i]  
        res = res.next  

    # Set the last node's next to None
    res.next = None  
    return save