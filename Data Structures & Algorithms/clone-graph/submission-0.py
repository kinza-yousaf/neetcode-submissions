"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        visited = {}
        
        def dfs(node):
            if not node:
                return None
            if visited.get(node):
                return visited.get(node)
            copy = Node(node.val)
            visited[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        dfs(node)
        return visited[node] if node else None
            
            

        

