class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def dfs(node, parent = -1):
            if node in visited:
                return True
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if dfs(nei, node):
                    return True
            return False
                
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            visited = set()
            if dfs(a, - 1):
                return [a, b]
        return []

        