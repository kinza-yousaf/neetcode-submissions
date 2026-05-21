# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        
        second = s.next
        s.next = None # break link between first and second half

        # reverse second half
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        firstH, secondH = head, prev

        while secondH:
            tmp1, tmp2 = head.next, secondH.next
            head.next = secondH
            secondH.next = tmp1
            head, secondH = tmp1, tmp2
        
        return
        
        
        
        