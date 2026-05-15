class ListNode:
    def __init__(self, val: int, next_node: Optional["Node"] = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.dummy_head = ListNode(0)
        self.tail = self.dummy_head
    
    def get(self, index: int) -> int:
        curr = self.dummy_head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.dummy_head.next
        self.dummy_head.next = new_node
        if not new_node.next: # if first insert set tail
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        prev = self.dummy_head
        i = 0 # i.next is node we want
        while i < index and prev:
            i += 1
            prev = prev.next
        # i == index or prev is None
        if prev and prev.next:
            # if removing tail update pointer
            if prev.next == self.tail:
                self.tail = prev
            prev.next = prev.next.next # removed node at index
            return True
        return False

    def getValues(self) -> List[int]:
        arr = []
        curr = self.dummy_head.next
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr