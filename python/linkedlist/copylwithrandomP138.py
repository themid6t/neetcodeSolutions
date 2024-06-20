"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return 

        hashmap = {}
        curr = head
        while curr:
            hashmap[curr] = Node(curr.val)
            curr = curr.next
        
        newL = hashmap[head]
        for key, _ in hashmap.items():
            if key.next:
                hashmap[key].next = hashmap[key.next]
        
            if key.random:
                hashmap[key].random = hashmap[key.random]
        
        return newL