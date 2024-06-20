# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def reverseList(head):
#     """
#     :type head: ListNode
#     :rtype: ListNode
#     """
#     prev, cur = None, head
#     while cur:
#         nxt = cur.next
#         cur.next = prev
#         prev = cur
#         cur = nxt
#     return prev

def reverseList(head):
    if not head:
        return None
    if head.next:
        newhead = reverseList(head.next)
        head.next.next = head
    head.next = None
    return newhead

ll = [1,2,3,4,5]
reverseList(ll)
