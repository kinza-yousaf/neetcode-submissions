class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colSet = set()
        posDiagSet = set()
        negDiagSet = set()

        # wrong: creates n references to the same row board = [["."] * n] * n
        board = [["."] * n for _ in range(n)] 

        print(board)
        boards = []

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                boards.append(copy)
                return
            for c in range(n):
                if (r + c) in posDiagSet or c in colSet or (r - c) in negDiagSet:
                    continue
                colSet.add(c)
                posDiagSet.add(r + c)
                negDiagSet.add(r - c)
                
                board[r][c] = "Q"

                backtrack(r + 1)

                colSet.remove(c)
                posDiagSet.remove(r + c)
                negDiagSet.remove(r - c)
                board[r][c] = "."
 
        backtrack(0)

        return boards
