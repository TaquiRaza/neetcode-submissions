class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        
    def append(self, value: int) -> None:
        node = Node(value)
        prev = self.tail.prev
        # connect left
        prev.next = node
        node.prev = prev
        # connect right
        node.next = self.tail
        self.tail.prev = node

    def appendleft(self, value: int) -> None:
        node = Node(value)
        nxt = self.head.next
        # connect left
        self.head.next = node
        node.prev = self.head
        # connect right
        node.next = nxt
        nxt.prev = node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        self.tail = self.tail.prev
        self.tail.next = None
        return self.tail.value
        
    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        self.head = self.head.next
        self.head.prev = None
        return self.head.value