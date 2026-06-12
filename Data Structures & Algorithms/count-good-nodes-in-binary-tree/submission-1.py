# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([[root, root.val]])
        cnt = 0

        while q:
            node, maxVal = q.popleft()
            if node.val >= maxVal:
                cnt += 1
            if node.left:
                q.append([node.left, max(maxVal, node.left.val)])
            if node.right:
                q.append([node.right, max(maxVal, node.right.val)])
        return cnt