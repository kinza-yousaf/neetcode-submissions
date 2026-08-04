class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        q = deque([])
        for r in [0, ROWS - 1]:
            for c in range(0, COLS):
                if board[r][c] == "O":
                    q.append((r, c))
                    board[r][c] = "T"
        for c in [0, COLS - 1]:
            for r in range(0, ROWS):
                if board[r][c] == "O":
                    q.append((r, c))
                    board[r][c] = "T"

        directions =[[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            qLen = len(q)
            for _ in range(qLen):
                r, c = q.pop()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == "O":
                        board[nr][nc] = "T"
                        q.append((nr, nc))
        print(board)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
        
           
                
