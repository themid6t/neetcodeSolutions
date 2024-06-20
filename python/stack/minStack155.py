class Node:
    def __init__(self, data, min_val) -> None:
        self.data = data
        self.next = None
        self.min_val = min_val

class MinStack:
    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if self.head is None: 
            self.head = Node(val, val)
            return
        new_node = Node(val, min(val, self.head.min_val))
        new_node.next = self.head
        self.head = new_node

    def pop(self) -> None:
        if self.head is None: raise Exception("Underflow")
        val = self.head.data
        self.head = self.head.next
        return val
    
    def top(self) -> int:
        if self.head is None: return None
        return self.head.data

    def getMin(self) -> int:
        if self.head is None: return None
        return self.head.min_val
