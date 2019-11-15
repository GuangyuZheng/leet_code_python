from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        height = len(matrix)
        if height == 0:
            return output
        wide = len(matrix[0])
        if wide == 0:
            return output
        wall = [[False for i in range(wide)] for j in range(height)]
        x, y = 0, 0
        direction = 0  # 0 left 1 down 2 right 3 up
        error_cnt = 0
        output.append(matrix[x][y])
        wall[x][y] = True
        while error_cnt < 2:
            old_x, old_y = x, y
            if direction == 0:
                x, y = x, y+1
                if y >= wide or wall[x][y] is True:
                    x, y = old_x, old_y
                    direction = 1
                    error_cnt += 1
                    continue
            if direction == 1:
                x, y = x+1, y
                if x >= height or wall[x][y] is True:
                    x, y = old_x, old_y
                    direction = 2
                    error_cnt += 1
                    continue
            if direction == 2:
                x, y = x, y-1
                if y < 0 or wall[x][y] is True:
                    x, y = old_x, old_y
                    direction = 3
                    error_cnt += 1
                    continue
            if direction == 3:
                x, y = x-1, y
                if x < 0 or wall[x][y] is True:
                    x, y = old_x, old_y
                    direction = 0
                    error_cnt += 1
                    continue
            output.append(matrix[x][y])
            wall[x][y] = True
            error_cnt = 0
        return output


# Shorter codes
class SolutionV2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        height = len(matrix)
        if height == 0:
            return output
        wide = len(matrix[0])
        if wide == 0:
            return output
        wall = [[False for i in range(wide)] for j in range(height)]
        x, y = 0, 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        di = 0
        error_cnt = 0
        output.append(matrix[x][y])
        wall[x][y] = True
        while error_cnt < 2:
            old_x, old_y = x, y
            x, y = x + dx[di], y + dy[di]
            if x >= height or x < 0 or y >= wide or y < 0 or wall[x][y] is True:
                x, y = old_x, old_y
                di = (di+1) % 4
                error_cnt += 1
                continue
            output.append(matrix[x][y])
            wall[x][y] = True
            error_cnt = 0
        return output


# simulate layer by layer
class SolutionV3:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        output = []
        height, wide = len(matrix), len(matrix[0])
        xlo, ylo = 0, 0
        xhi, yhi = height-1, wide-1
        while xlo <= xhi and ylo <= yhi:
            for i in range(ylo, yhi+1):
                output.append(matrix[xlo][i])
            for i in range(xlo+1, xhi+1):
                output.append(matrix[i][yhi])

            # If xlo == xhi or ylo == yhi, then the outputs of this layer don't contain Rightward and Upward
            if xlo < xhi and ylo < yhi:
                for i in range(yhi-1, ylo-1, -1):
                    output.append(matrix[xhi][i])
                for i in range(xhi-1, xlo, -1):
                    output.append(matrix[i][ylo])
            xlo += 1
            ylo += 1
            xhi -= 1
            yhi -= 1
        return output
