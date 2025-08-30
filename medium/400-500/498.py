"""
Diagonal Traverse.

Развернуть матрицу целых чисел в одномерный массив при движении по диагонали.
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] -> [1, 2, 4, 7, 5, 3, 6, 8, 9]

Сначала проходимся по 1-й строчке и от каждой позиции движемся по диагонали
влево и вниз, добавляя элементы в массив curr. Если reverse = False, то есть
порядок следования из правого верхнего угла в левый нижний, то добавляем curr
в исходном виде к ответу. В ином случае, разворачиваем curr перед добавлением.
После прохода по диагонали меняем значение reverse на противоположное. Затем
повторяем такой же цикл, проходя по элементам последнего столбца, кроме 1-го.

Лучшее решение: 6 ms, 19.74 Mb
"""


class Solution:

    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        m = len(mat)
        n = len(mat[0])
        arr = []
        reverse = True

        def __func(row: int, col: int, m: int, reverse: bool):
            curr = []
            while col >= 0 and row < m:
                curr.append(mat[row][col])
                row += 1
                col -= 1
            if reverse:
                curr = curr[::-1]
            arr.extend(curr)
            return not reverse

        for col in range(n):
            row = 0
            reverse = __func(row, col, m, reverse)
        for row in range(1, m):
            col = n - 1
            reverse = __func(row, col, m, reverse)
        return arr
