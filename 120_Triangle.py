from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 0:
            return 0
        for i in range(n):
            for j in range(i + 1):
                if i > 0:
                    if j == 0:
                        triangle[i][j] += triangle[i - 1][j]
                    elif j == i:
                        triangle[i][j] += triangle[i - 1][j - 1]
                    else:
                        tmp = triangle[i][j]
                        triangle[i][j] = min(tmp + triangle[i - 1][j], tmp + triangle[i - 1][j - 1])
        result = min(triangle[-1])
        return result
