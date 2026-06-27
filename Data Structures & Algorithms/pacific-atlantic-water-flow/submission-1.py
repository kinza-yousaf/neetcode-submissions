class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pacSet = set()
        atlSet = set()
        res = []


        def dfs(r, c, visitedSet, prevHeight):
            if (r not in range(ROWS) or c not in range(COLS) or
                (r, c) in visitedSet or heights[r][c] < prevHeight
                ):
                return
            visitedSet.add((r, c)) # reachable by the ocean
            dfs(r + 1, c, visitedSet, heights[r][c])
            dfs(r - 1, c, visitedSet, heights[r][c])
            dfs(r, c + 1, visitedSet, heights[r][c])
            dfs(r, c - 1, visitedSet, heights[r][c])
        
        # for r in range(ROWS):
        #     pacSet.add((r, 0))
        #     atlSet.add((r, COLS - 1))

        # for c in range(COLS):
        #     pacSet.add((0, c))
        #     atlSet.add((ROWS - 1, c))

        for r in range(ROWS):
            dfs(r, 0, pacSet, heights[r][0])
            dfs(r, COLS - 1, atlSet, heights[r][COLS - 1])

        for c in range(COLS):
            dfs(0, c, pacSet, heights[0][c])
            dfs(ROWS - 1, c, atlSet, heights[ROWS - 1][c])

        for r, c in (pacSet & atlSet):
            res.append([r, c])
        print(res)
        return res




            