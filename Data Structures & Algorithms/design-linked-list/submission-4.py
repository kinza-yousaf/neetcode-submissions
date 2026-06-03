class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)
    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        prev, curr = self.head, self.head.next
        for i in range(index):
            prev = curr
            curr = curr.next
        return curr.val
        
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        prev, curr = self.head, self.head.next
        for i in range(index):
            prev = curr
            curr = curr.next
        prev.next = ListNode(val, prev.next)
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        prev, curr = self.head, self.head.next
        for i in range(index):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        self.size -= 1

