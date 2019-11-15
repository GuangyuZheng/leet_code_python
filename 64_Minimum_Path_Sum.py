from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mat = [[-1 for i in range(n)] for j in range(m)]
        mat[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0:
                    if j > 0:
                        mat[i][j] = mat[i][j - 1] + grid[i][j]
                        continue
                elif j == 0:
                    if i > 0:
                        mat[i][j] = mat[i - 1][j] + grid[i][j]
                        continue
                else:
                    mat[i][j] = min(mat[i][j - 1] + grid[i][j], mat[i - 1][j] + grid[i][j])
        return mat[-1][-1]
