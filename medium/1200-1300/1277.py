"""
Count Square Submatrices with All Ones.

Найти количество квадратных подматриц, состоящих только из единиц.

Заведем матрицу dp, каждый элемент которой показывает размер квадратной
подматрица единиц, которая в нем заканчивается. Для этого выбираем минимум
из соседа слева, сверху и под диагонали лево-верх и прибавляем 1, если элемент
матрицы равен 1. Размеры dp на 1 больше, чем у исходной матрицы, чтобы не
делать проверки на выход за пределы матрицы. Ответом будет сумма всех
элементов dp.

Лучшее решение: 51 ms, 20.34 Mb
"""


class Solution:

    def countSquares(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    idp, jdp = i + 1, j + 1
                    dp[idp][jdp] = (
                        min(dp[i + 1][j], dp[i][j], dp[i][j + 1])
                        + 1
                    )
        return sum(sum(e) for e in dp)
