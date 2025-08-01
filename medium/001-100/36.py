"""
Valid Sudoku.

Проверить на валидность текущее состояние поля судоку.

Лучшее решение: 3 ms, 17.97 Mb
"""


class Solution:

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        col_sets = [set() for _ in range(9)]
        cube_sets = [[set() for i in range(3)] for j in range(3)]
        for row in range(9):
            row_set = set()
            for col in range(9):
                val = board[row][col]
                if val == '.':
                    continue
                false_cond = (
                    val in row_set
                    or val in col_sets[col]
                    or val in cube_sets[row // 3][col // 3]
                )
                if false_cond:
                    return False
                row_set.add(val)
                col_sets[col].add(val)
                cube_sets[row // 3][col // 3].add(val)
        return True
