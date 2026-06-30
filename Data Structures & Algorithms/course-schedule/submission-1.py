class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
                
        visiting = set()
        visited = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                # already checked and good
                return True
            visiting.add(crs)
            for prereq in adj[crs]:
                if not dfs(prereq):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            return True

        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True