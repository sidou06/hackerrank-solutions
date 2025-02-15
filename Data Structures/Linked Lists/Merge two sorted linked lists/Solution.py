# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def mergeLists(head1, head2):
    # Initialize result list
    res = None  
    save = res  

    # Traverse both lists
    while head1 is not None and head2 is not None:
        # If result list is empty, initialize it
        if res is None:
            if head1.data <= head2.data:
                res = head1  
                head1 = head1.next  
            else:
                res = head2  
                head2 = head2.next  
            save = res  
        else:
            # Add the smaller node to the merged list
            if head1.data <= head2.data:
                res.next = head1  
                res = res.next  
                head1 = head1.next  
            else: 
                res.next = head2  
                res = res.next  
                head2 = head2.next  

    # Append the remaining nodes of the non-empty list
    if head1 is not None:
        if res is None:
            return head1  
        else:
            res.next = head1  
    else:
        if res is None:
            return head2  
        else:
            res.next = head2  

    return save