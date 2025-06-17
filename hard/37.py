"""
Sudoku Solver.

Необходимо решить судоку размером 9 * 9.

Лучшее решение: 1967 ms, 17.95 Mb
"""


class Solution:

    def __get_check_arrays(self, board: list[list[str]]):
        self.rows = [[True] * 9 for _ in range(9)]
        self.cols = [[True] * 9 for _ in range(9)]
        self.thirds = [[True] * 9 for _ in range(9)]
        self.empty_cnt = 0
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val.isdigit():
                    num = int(val)
                    self.rows[i][num - 1] = False
                    self.cols[j][num - 1] = False
                    self.thirds[i // 3 * 3 + j // 3][num - 1] = False
                else:
                    self.empty_cnt += 1

    def rec(self, board: list[list[str]], curr_row: int = 0):
        for i in range(curr_row, 9):
            for j in range(9):
                if board[i][j] == '.':
                    cnt = 0
                    for k in range(9):
                        cnd = (
                            self.rows[i][k]
                            and self.cols[j][k]
                            and self.thirds[i // 3 * 3 + j // 3][k]
                        )
                        if cnd:
                            cnt += 1
                            self.rows[i][k] = False
                            self.cols[j][k] = False
                            self.thirds[i // 3 * 3 + j // 3][k] = False
                            board[i][j] = str(k + 1)
                            status = self.rec(board=board, curr_row=i)
                            if status == 'wrong':
                                self.rows[i][k] = True
                                self.cols[j][k] = True
                                self.thirds[i // 3 * 3 + j // 3][k] = True
                                board[i][j] = '.'
                                cnt -= 1
                    if not cnt:
                        return 'wrong'
        return 'ok'

    def solveSudoku(self, board: list[list[str]]) -> None:
        self.__get_check_arrays(board=board)
        self.rec(board=board)
