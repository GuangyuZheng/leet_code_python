from typing import List
import copy


# A straight forward solution using O(m*n) space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        old_status = copy.deepcopy(matrix)
        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0 and old_status[x][y] == 0:
                    for i in range(m):
                        matrix[i][y] = 0
                    for j in range(n):
                        matrix[x][j] = 0


# o(m+n) space
class SolutionV2:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        xs = set()
        ys = set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    xs.add(i)
                    ys.add(j)
        for i in range(m):
            for j in range(n):
                if i in xs or j in ys:
                    matrix[i][j] = 0


# Brute Force o(1) space
class SolutionV3:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        MODIFY = -10e9
        m, n = len(matrix), len(matrix[0])
        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0:
                    for i in range(m):
                        if matrix[i][y] != 0:
                            matrix[i][y] = MODIFY
                    for i in range(n):
                        if matrix[x][i] != 0:
                            matrix[x][i] = MODIFY

        for x in range(m):
            for y in range(n):
                if matrix[x][y] == MODIFY:
                    matrix[x][y] = 0


# Efficient o(1) space o(m*n) time
class SolutionV4:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        is_col = False
        for x in range(m):
            if matrix[x][0] == 0:
                is_col = True
            for y in range(1, n):
                if matrix[x][y] == 0:
                    matrix[x][0] = 0
                    matrix[0][y] = 0

        for x in range(1, m):
            for y in range(1, n):
                if matrix[x][0] == 0 or matrix[0][y] == 0:
                    matrix[x][y] = 0

        if matrix[0][0] == 0:
            for i in range(n):
                matrix[0][i] = 0

        if is_col:
            for i in range(m):
                matrix[i][0] = 0


# Official Solution the same as V4
class SolutionOfficial(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well
        if is_col:
            for i in range(R):
                matrix[i][0] = 0
