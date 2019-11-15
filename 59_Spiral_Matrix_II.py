from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for i in range(n)]
        current, end = 1, n*n
        xlo, ylo = 0, 0
        xhi, yhi = n-1, n-1
        while xlo <= xhi and ylo <= yhi:
            for y in range(ylo, yhi+1):
                matrix[xlo][y] = current
                current += 1
            for x in range(xlo+1, xhi+1):
                matrix[x][yhi] = current
                current += 1
            if xlo < xhi and ylo < yhi:
                for y in range(yhi-1, ylo-1, -1):
                    matrix[xhi][y] = current
                    current += 1
                for x in range(xhi-1, xlo, -1):
                    matrix[x][ylo] = current
                    current += 1
            xlo += 1
            ylo += 1
            xhi -= 1
            yhi -= 1
        assert current-1 == end
        return matrix
