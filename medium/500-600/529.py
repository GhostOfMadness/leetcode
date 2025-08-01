"""
Minesweeper.

Обновить поле для игры в сапера после клика по заданной клетке.

Лучшее решение: 8 ms, 18.49 Mb
"""


from collections import deque


class Solution:

    def __check_neighbors(self, row: int, col: int, board: list[list[int]]):
        shifts_i = [0, -1, -1, -1, 0, 1, 1, 1]
        shifts_j = [-1, -1, 0, 1, 1, 1, 0, -1]
        bombs_cnt = 0
        neighbors = []
        for k in range(8):
            i = row + shifts_i[k]
            j = col + shifts_j[k]
            if 0 <= i < self.m and 0 <= j < self.n:
                if board[i][j] == 'M':
                    bombs_cnt += 1
                if board[i][j] == 'E' and not self.visited[i][j]:
                    neighbors.append((i, j))
        return bombs_cnt, neighbors

    def updateBoard(
        self,
        board: list[list[str]],
        click: list[int],
    ) -> list[list[str]]:
        row, col = click
        self.m = len(board)
        self.n = len(board[0])
        self.visited = [[False] * self.n for _ in range(self.m)]
        self.visited[row][col] = True
        if board[row][col] == 'M':
            board[row][col] = 'X'
        elif board[row][col] == 'E':
            neighbors = deque([(row, col)])
            while neighbors:
                r, c = neighbors.popleft()
                curr_cnt, curr_neighbors = self.__check_neighbors(r, c, board)
                if curr_cnt:
                    board[r][c] = str(curr_cnt)
                else:
                    board[r][c] = 'B'
                    for e in curr_neighbors:
                        neighbors.append(e)
                        self.visited[e[0]][e[1]] = True
        return board
