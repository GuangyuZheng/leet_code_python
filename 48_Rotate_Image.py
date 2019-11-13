from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range((n+1)//2):
            for j in range(i, n-i-1):
                x, y = i, j
                next_x, next_y = y, n-1-x
                old_value = matrix[x][y]
                old_next_value = matrix[next_x][next_y]
                for k in range(4):
                    matrix[next_x][next_y] = old_value
                    x, y = next_x, next_y
                    old_value = old_next_value
                    next_x, next_y = y, n-1-x
                    old_next_value = matrix[next_x][next_y]


class SolutionV2:
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        return matrix

    def inverse(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][n - 1 - j]
                matrix[i][n - 1 - j] = tmp
        return matrix

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix = self.transpose(matrix)
        matrix = self.inverse(matrix)
