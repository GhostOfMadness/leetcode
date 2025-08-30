"""
Minimum Path Sum.

Найти минимальную стоимость пути из верхнего левого угла в правый нижний,
если ходить можно только вниз или вправо.

Используем динамическое программирование. Учитывая возможные направления
движения, достаточно хранить массив ответов только для предыдущей строки.
dp[i][j] = минимальная стоимость пути к точке (i, j).
dp[i][j] = grid[i][j] + min(dp[i][j - 1], dp[i - 1][j]). При использовании
одномерного массива dp, значения которого будут обновляться на каждом шаге
получаем dp[j] = grid[i][j] + min(dp[j], dp[j - 1]).

Лучшее решение: 2 ms, 18.69 Mb
"""


from itertools import accumulate


class Solution:

    def minPathSum(self, grid: list[list[int]]) -> int:
        dp = list(accumulate(grid[0]))
        m, n = len(grid), len(grid[0])
        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                add = dp[j] if dp[j] < dp[j - 1] else dp[j - 1]
                dp[j] = add + grid[i][j]
        return dp[n - 1]
