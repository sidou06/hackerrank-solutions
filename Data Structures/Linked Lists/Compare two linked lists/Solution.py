# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def compare_lists(llist1, llist2):
    # Assume lists are identical initially
    same = True  

    # Traverse both lists simultaneously
    while llist1 is not None and llist2 is not None and same:
        # Check if corresponding nodes have different data
        if llist1.data != llist2.data:
            same = False  
        llist1 = llist1.next  
        llist2 = llist2.next  

    # If a difference was found, return 0
    if not same:
        return 0  
    # If both lists reached the end together, they are identical
    elif llist1 is None and llist2 is None:
        return 1  
    # If one list is longer than the other, they are different
    else:
        return 0  