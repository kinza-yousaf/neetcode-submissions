class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
                
        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            visiting.add(crs)
            for prereq in adj[crs]:
                if not dfs(prereq):
                    return False
            visiting.remove(crs)
            return True

        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True