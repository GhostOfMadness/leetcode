"""
Equal Sum Grid Pertition I.

Дана матрица положительных целых чисел размера n * m. Выяснить, можно ли
разделить эту матрицу на 2 части по вертикали или горизонтали таким образом,
чтобы сумма элементов в каждой части была одинакова.

Считаем префиксные суммы по строкам и столбцам. Если какая-то из этих сумм
совпадает с половиной суммы всех элементов, то разбиение возможно.

Лучшее решение: 135 ms, 43.16 Mb
#matrix #prefix_sum
"""


class Solution:

    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        rows = [0] * (n + 1)
        cols = [0] * (m + 1)
        for i in range(n):
            rows[i + 1] = rows[i] + sum(grid[i])
        total = rows[n]
        if total % 2:
            return False
        half = total // 2
        i = 1
        while rows[i] < half:
            i += 1
        if rows[i] == half:
            return True
        for j in range(m):
            cols[j + 1] = cols[j] + sum(grid[i][j] for i in range(n))
        j = 1
        while cols[j] < half:
            j += 1
        return cols[j] == half
