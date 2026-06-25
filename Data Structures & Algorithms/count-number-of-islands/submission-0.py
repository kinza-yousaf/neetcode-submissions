class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        cnt = 0

        def dfs(r, c):
            if (r < 0 or r >= ROWS or
            c < 0 or c >= COLS or 
            grid[r][c] == "0"
            ):
                return

            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    cnt += 1
                    dfs(r, c) # go ahead and mark all nodes as 0 to avoid revisiting or double counitng

        return cnt

        
                
