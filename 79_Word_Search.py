from typing import List


class Solution:
    def __init__(self, ):
        self.visited = None

    def reset(self, board):
        r, c = len(board), len(board[0])
        self.visited = [[0 for i in range(c)] for j in range(r)]

    def search(self, board, curr_x, curr_y, word, pos):
        r, c = len(board), len(board[0])

        if pos == len(word):
            return True

        choice_x = [-1, 1, 0, 0]
        choice_y = [0, 0, -1, 1]

        for i in range(4):
            x, y = curr_x + choice_x[i], curr_y + choice_y[i]
            if 0 <= x < r and 0 <= y < c:
                if board[x][y] == word[pos] and self.visited[x][y] == 0:
                    self.visited[x][y] = 1
                    if self.search(board, x, y, word, pos + 1) is True:
                        return True
                    else:
                        self.visited[x][y] = 0
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0:
            return False
        if len(board[0]) == 0:
            return False
        self.reset(board)
        r, c = len(board), len(board[0])
        for x in range(r):
            for y in range(c):
                if board[x][y] == word[0]:
                    self.visited[x][y] = 1
                    if self.search(board, x, y, word, 1) is True:
                        return True
                    else:
                        self.visited[x][y] = 0
        return False
