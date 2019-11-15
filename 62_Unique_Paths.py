class Solution:
    # O(n^2) space complexity
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            paths[0][i] = 1
        for i in range(m):
            paths[i][0] = 1
        for x in range(1, m):
            for y in range(1, n):
                paths[x][y] += paths[x-1][y] + paths[x][y-1]
        return paths[m-1][n-1]

    # O(2*n) space complexity
    def uniquePathsV2(self, m: int, n: int) -> int:
        prev = [1] * n
        current = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                current[j] = prev[j] + current[j-1]
            prev = current
        return current[-1]

    # O(n) space complexity
    def uniquePathsV3(self, m: int, n: int) -> int:
        current = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                current[j] += current[j - 1]
        return current[-1]
