class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        q = deque([])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c,0))
                    visited.add((r, c))
        while q:
            r, c, dist = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visited or grid[nr][nc] == -1:
                    continue
                grid[nr][nc] = min(grid[nr][nc], 1 + dist)
                visited.add((nr, nc))
                q.append((nr, nc, 1 + dist))
