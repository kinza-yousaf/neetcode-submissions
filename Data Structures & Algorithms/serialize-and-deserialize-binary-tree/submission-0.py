# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        comb = []
        def dfs(node):
            if not node:
                comb.append("N")
                return
            comb.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(comb)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(",")
        q = deque(arr)
        
        def dfs():
            val = q.popleft()
            if val == "N":
                return None
            node = TreeNode(int(val), dfs(), dfs())
            return node
        return dfs()


