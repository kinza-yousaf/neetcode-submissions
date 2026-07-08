class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # transpose
        for i in range(n):
            for j in range(i):
                if i == j:
                    continue
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        # reverse rows
        for row in matrix:
            l, r = 0, len(row) - 1
            while l < r:
                tmp = row[l]
                row[l] = row[r]
                row[r] = tmp
                l += 1
                r -= 1
        
        