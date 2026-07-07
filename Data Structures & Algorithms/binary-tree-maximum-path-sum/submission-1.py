# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def dfs(node):
            nonlocal res
            if not node:
                return float("-inf")
            right = dfs(node.right)
            left = dfs(node.left)
            res = max(res, left + node.val, right + node.val, left + node.val + right, node.val)
            return max(left + node.val, right + node.val, node.val)
        dfs(root) 
        return res