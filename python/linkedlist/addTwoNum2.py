# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumofl = ListNode()
        head = sumofl

        carry = 0
        while l1 or l2:
            if l1 is None:
                ans = l2.val + carry
                l2 = l2.next
            elif l2 is None:
                ans = l1.val + carry
                l1 = l1.next
            else:
                ans = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next

            if ans >= 10:
                carry = ans // 10
                ans %= 10
            else:
                carry = 0

            head.next = ListNode(ans)
            head = head.next

        if carry > 0:
            head.next = ListNode(carry)
        return sumofl.next
