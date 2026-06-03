class ListNode:
    # Using sentinel
    def __init__(self, val: int, next: ListNode = None, prev: ListNode = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0, None, self.head)
        self.head.next = self.tail
        self.size = 0

        

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
        prev.next = ListNode(val, curr, prev)
        curr.prev = prev.next
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        prev, curr = self.head, self.head.next
        for i in range(index):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        curr.next.prev = prev
        self.size -= 1


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)