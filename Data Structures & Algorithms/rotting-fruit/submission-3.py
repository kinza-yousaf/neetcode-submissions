class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visited = set()
        fresh = 0
        mins = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    visited.add((i, j))
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        print(fresh)
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                print(r, c)
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nr >= ROWS or
                        nc < 0 or nc >= COLS or
                        (nr, nc) in visited or grid[nr][nc] == 0):
                        continue
                    if grid[nr][nc] == 1:
                        fresh -= 1
                        visited.add((nr, nc))
                        q.append((nr, nc))
                    if fresh == 0:
                        break
            if q:
                mins += 1
        return mins if fresh == 0 else -1
