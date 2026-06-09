# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mergedList = ListNode(0, None)
        mergedList = mergedList.next
        for l in lists:
            mergedList = self.mergeSortedLists(mergedList, l)
        return mergedList
        

    def mergeSortedLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0, None)
        list3 = sentinel
        while list1 and list2:
            if list1.val < list2.val:
                list3.next = ListNode(list1.val, None)
                list1 = list1.next
            else:
                list3.next = ListNode(list2.val, None)
                list2 = list2.next
            list3 = list3.next
        list3.next = list1 or list2
        return sentinel.next