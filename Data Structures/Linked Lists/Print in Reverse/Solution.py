#
# Complete the 'reversePrint' function below.
#
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

def reversePrint(llist):
    # Store node values in a list
    datas = []  
    while llist is not None:
        datas.append(llist.data)
        llist = llist.next  

    # Print values in reverse order
    for i in range(len(datas) - 1, -1, -1):
        print(datas[i])