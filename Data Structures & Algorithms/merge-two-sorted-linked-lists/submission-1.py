# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = ListNode(0, None)
        list3 = tmp
        while list1 and list2:
            if list1.val < list2.val:
                list3.next = ListNode(list1.val, None)
                list1 = list1.next
            else:
                list3.next = ListNode(list2.val, None)
                list2 = list2.next
            list3 = list3.next
        list3.next = list1 or list2
        return tmp.next