from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        if r == 0:
            return False
        c = len(matrix[0])
        total_num = r * c
        left = 0
        right = total_num-1

        while left <= right:
            mid = (left + right) // 2
            x = mid // c
            y = mid - c * x
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                left = mid+1
            else:
                right = mid-1
        return False
