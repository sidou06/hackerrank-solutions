# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    # Pointer to traverse the second linked list
    tmp2 = head2  
    
    # Traverse the second linked list
    while tmp2 is not None:
        # Pointer to traverse the first linked list
        tmp1 = head1  
        
        # Traverse the first linked list to check for intersection
        while tmp1 is not None and tmp1 != tmp2:
            tmp1 = tmp1.next  
        
        # If intersection is found, return the data of the merge node
        if tmp1 == tmp2:
            return tmp1.data  
        
        # Move to the next node in the second linked list
        tmp2 = tmp2.next