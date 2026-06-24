class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        def dfs(i, j, word):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or word == "" or (i,j) in visited:
                return False
            if board[i][j] == word[0]:
                visited.add((i, j))
                if len(word) == 1:
                    return True
                found = dfs(i + 1, j, word[1:]) or dfs(i - 1, j, word[1:]) or dfs(i, j + 1, word[1:]) or dfs(i, j - 1, word[1:])
                visited.remove((i, j))
                return found
            return False
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, word):
                    print("hi")
                    return True

        return False