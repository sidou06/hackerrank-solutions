# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def printLinkedList(head):
    # Traverse the linked list until the end
    while head != None:
        # Print the current node's data
        print(head.data)  
        # Move to the next node
        head = head.next  