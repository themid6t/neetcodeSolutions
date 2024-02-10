# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        pos, last = dummy, dummy
        idx = -n
        while last.next:
            if idx>=0: pos = pos.next
            last = last.next
            idx += 1

        pos.next = pos.next.next

        return dummy.next