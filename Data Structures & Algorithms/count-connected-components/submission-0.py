class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor in visited:
                    continue
                dfs(neighbor)
            return
                
            
        components = 0
        for i in range(n):
            if i in visited:
                continue
            components += 1
            dfs(i)

        return components