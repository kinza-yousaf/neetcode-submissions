# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = lists
        while len(res) > 1:
            merged = []
            for i in range(0, len(res), 2):
                l2 = res[i+1] if i+1 < len(res) else None
                merged.append(self.mergeSortedLists(res[i], l2))
            res = merged
        return res[0] if res else None

    def mergeSortedLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0, None)
        list3 = sentinel
        while list1 and list2:
            if list1.val < list2.val:
                list3.next = list1
                list1 = list1.next
            else:
                list3.next = list2
                list2 = list2.next
            list3 = list3.next
        list3.next = list1 or list2
        return sentinel.next