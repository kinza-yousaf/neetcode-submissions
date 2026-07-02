class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {(m - 1, n - 1): 1}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[i, j]
            if i not in range(m) or j not in range(n):
                return 0
            memo[(i, j)] = dfs(i + 1, j) + dfs(i, j + 1)
            return memo[(i, j)]
        print(memo)
        return dfs(0, 0)