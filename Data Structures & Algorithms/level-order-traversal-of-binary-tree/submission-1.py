# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        res = [[root.val]] if root else []
        while q:
            lst = []
            for _ in range(len(q)):
                node = q.popleft()
                if node and node.left:
                    lst.append(node.left.val)
                    q.append(node.left)
                if node and node.right:
                    lst.append(node.right.val)
                    q.append(node.right)
            if lst:
                res.append(lst)
        return res