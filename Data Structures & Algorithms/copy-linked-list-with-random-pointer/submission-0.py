"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        oldToCopyMap = {}
        while cur:
            oldToCopyMap[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldToCopyMap[cur]
            copy.next = oldToCopyMap[cur.next] if cur.next else None
            copy.random = oldToCopyMap[cur.random] if cur.random else None
            cur = cur.next
        return oldToCopyMap.get(head)


        
        