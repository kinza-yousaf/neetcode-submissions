class ListNode:
    def __init__(self, val: int, next: ListNode = None, prev: ListNode = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if self.size == 0 or index >= self.size:
            return -1
        curr = self.head
        while index > 0 and curr:
            curr = curr.next
            index -= 1
        return curr.val if curr else -1


    def addAtHead(self, val: int) -> None:
        if self.size == 0:
            self.head = ListNode(val)
            self.tail = self.head
            self.size += 1
        else:
            tmp = ListNode(val, self.head, None)
            self.head.prev = tmp
            self.head = tmp
            self.size += 1

        

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.head = ListNode(val)
            self.tail = self.head
            self.size += 1
        else:
            tmp = ListNode(val, None, self.tail)
            self.tail.next = tmp
            self.tail = tmp
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        elif index == self.size:
            tmp = ListNode(val, None, self.tail)
            self.tail.next = tmp
            self.tail = tmp
            self.size += 1
            return
        else:
            tmp = ListNode(val, None, None)
            curr = self.head
            prev = curr.prev
            if index == 0:
                self.head = tmp
            while index > 0 and curr:
                prev = curr
                curr = curr.next
                index -= 1

            tmp.next = curr
            tmp.prev = tmp
            curr.prev = tmp
            prev.next = tmp
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if self.size == 0 or index >= self.size:
            return
        prev, curr = None, self.head
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return
        if index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return 

        while index > 0 and (prev or curr):
            prev = curr
            curr = curr.next
            index -= 1
        prev.next = curr.next
        curr.next.prev = prev
        curr.next = None
        curr.prev = None
        self.size -= 1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)