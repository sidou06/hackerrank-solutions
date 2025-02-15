# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtTail(head, data):
    # Create a new node with the given data
    res = SinglyLinkedListNode(data)
    res.next = None  

    # If the linked list is empty, return the new node as the head
    if head == None:
        return res  

    # Traverse the linked list to find the last node
    save = head  
    while head.next != None:
        head = head.next  

    # Append the new node at the end of the linked list
    head.next = res  

    # Return the original head of the linked list
    return save