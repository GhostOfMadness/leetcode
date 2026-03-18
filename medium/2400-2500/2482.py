"""
Difference Between Ones and Zeros in Row and Column.

Дана бинарная матрица размера m * n. Найти матрицу diff такого же размера,
где diff[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j].
onesRow[i] и onesCol[j] - количество единиц в i-й строке и j-м столбце
исходной матрицы, zerosRow[i] и zerosCol[j] - количество нулей.

Создаем массивы rows и cols, где будем хранить количество единиц для каждой
строки и столбца. Проходимся по матрице и заполняем массивы. diff[i][j] =
rows[i] + cols[j] - (n - rows[i]) - (m - cols[j]) = 2 * (rows[i] + cols[j])
- m - n. Заполняем матрицу diff по формуле и возвращаем ее.

Лучшее решение: 124 ms, 48.80 Mb
#matrix #array #simulation
"""


class Solution:

    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        m = len(grid)
        n = len(grid[0])
        rows = [0] * m
        cols = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rows[i] += 1
                    cols[j] += 1
        diff = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                diff[i][j] = 2 * (rows[i] + cols[j]) - m - n
        return diff
