from linkedList import Llist, Node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeTwoLists(list1, list2):
    head = Node
    tail = head
    while list1 and list1:
        if list1.data <= list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    if list1: tail.next = list1
    else: tail.next = list2
    return head.next




ar1 = [1,2,4]
ar2 = [1,3,4]

l1 = Llist()
l2 = Llist()

l1.insertFromArray(ar1)
l2.insertFromArray(ar2)

h = mergeTwoLists(l1.head, l2.head)

while h.next != None: h = h.next; 