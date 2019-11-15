from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        mat = [[0 for i in range(n)] for j in range(m)]
        mat[-1][-1] = 1 if obstacleGrid[-1][-1] != 1 else 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if obstacleGrid[i][j] != 1:
                    if i+1 < m:
                        mat[i][j] += mat[i+1][j]
                    if j+1 < n:
                        mat[i][j] += mat[i][j+1]
        return mat[0][0]
