class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # bit mask ops

        rows = [0] * 9 # each entry is a bit mask
        cols = [0] * 9 # each entry is a bit mask
        squares = [0] * 9 # each entry is a bit mask

        for i in range (9):
            for j in range (9):
                if board[i][j] == ".":
                    continue
                val = int(board[i][j]) - 1

                # 1 << n will cause the rest of the bits in rows[i] to be ignored
                if (1 << val) & (rows[i] | cols[j] | squares[((i // 3) * 3) + (j // 3)]):
                    return False

                rows[i] = rows[i] | (1 << val)
                cols[j] = cols[j] | (1 << val)
                squares[((i // 3) * 3) + (j // 3)] = squares[((i // 3) * 3) + (j // 3)] | (1 << val)
        
        return True      
        