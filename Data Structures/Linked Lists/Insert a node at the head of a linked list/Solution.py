# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtHead(llist, data):
    # Create a new node with the given data
    res = SinglyLinkedListNode(data)

    # Set the next pointer of the new node to the current head
    res.next = llist  

    # Return the new node as the new head of the linked list
    return res 