"""
Дана матрица целых положительных чисел размера m * n. Найти максимальную
сторону квадрата, в котором сумма всех строк, столбцов, главной и побочной
диагонали совпадают.

Алгоритм заключается в переборе всех возможных вариантов и выборе оптимального.
Для каждого квадрата необходимо знать сумму по строкам, столбцам и диагоналям.
Можно производить полный расчет заново при каждой проверке, а можно уменьшить
количество вычислений за счет использования префиксных сумм. Считаем префиксы
по каждому из нужных направлений. Размер каждой матрицы префиксов составляет
(m + 2) * (n + 1) для удобства расчетов и универсальности. Для расчета
префиксов идем по столбцам, чтобы за один проход заполнить все матрицы.
Максимальная сторона квадрата равна минимуму из размеров матрицы. Начинаем
перебирать варианты от максимального до 2-х включительно и проверять их.
Если какой-то вариант прошел проверку, то возвращаем найденную сторону
и заканчиваем цикл, не проверяя меньшие варианты. Внутри функции проверки
сначала находим сумму по первой строке, первому столбцу и диагоналям квадрата.
Если они не совпадают, то сразу возвращаем False. Если они равны, то проверяем
на равенство сначала строки, затем столбцы. Если оба этих цикла долшли до
конца, то проверка пройдена и сторона найдена.

Лучшее решение: 42 ms, 20.15 Mb
#matrix #prefix_sum
"""


class Solution:

    def getPrefixSums(self, grid: list[list[int]], m: int, n: int):
        rows = [[0] * (n + 1) for _ in range(m + 2)]
        cols = [[0] * (n + 1) for _ in range(m + 2)]
        diag1 = [[0] * (n + 1) for _ in range(m + 2)]
        diag2 = [[0] * (n + 1) for _ in range(m + 2)]
        for j in range(n):
            for i in range(m):
                rows[i + 1][j + 1] = grid[i][j] + rows[i + 1][j]
                cols[i + 1][j + 1] = grid[i][j] + cols[i][j + 1]
                diag1[i + 1][j + 1] = grid[i][j] + diag1[i + 2][j]
                diag2[i + 1][j + 1] = grid[i][j] + diag2[i][j]
        return rows, cols, diag1, diag2

    def checkSquare(
        self,
        i: int,
        j: int,
        k: int,
        rows: list[list[int]],
        cols: list[list[int]],
        diag1: list[list[int]],
        diag2: list[list[int]],
    ) -> bool:
        row_sum = rows[i + 1][j + k] - rows[i + 1][j]
        col_sum = cols[i + k][j + 1] - cols[i][j + 1]
        diag1_sum = diag1[i + 1][j + k] - diag1[i + k + 1][j]
        diag2_sum = diag2[i + k][j + k] - diag2[i][j]
        if not (row_sum == col_sum == diag1_sum == diag2_sum):
            return False
        for row in range(i + 1, i + k):
            curr = rows[row + 1][j + k] - rows[row + 1][j]
            if curr != row_sum:
                return False
        for col in range(j + 1, j + k):
            curr = cols[i + k][col + 1] - cols[i][col + 1]
            if curr != col_sum:
                return False
        return True

    def largestMagicSquare(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows, cols, diag1, diag2 = self.getPrefixSums(grid, m, n)
        max_k = min(m, n)
        for k in range(max_k, 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if self.checkSquare(i, j, k, rows, cols, diag1, diag2):
                        return k
        return 1
