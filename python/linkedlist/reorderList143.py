# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return head
        
        l1, l2 = self._splitList(head)
        l2 = self._reverseList(l2)
        
        # Merge the two lists ----------------
        while l1 and l2:
            l1_next = l1.next
            l2_next = l2.next

            l1.next = l2
            l2.next = l1_next

            l1 = l1_next
            l2 = l2_next
    
    def _splitList(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        l1 = head
        l2 = slow.next
        slow.next = None
        return l1, l2

    def _reverseList(self, head):
        newhead = head
        if head.next:
            newhead = self._reverseList(head.next)
            head.next.next = head
        head.next = None
        return newhead