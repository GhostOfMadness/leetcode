"""
Number of Islands.

Дана матрица размером m * n, заполненная символами '1' и '0'. '1' - участок
суши, '0' - океан. Островом считается набор связанных друг с другом по
вертикали или горизонтали участков суши. Найти количество островов.

Сначала сделаем вокруг исходной матрицы рамку из нулей, а заодно переведем
все строковые значения в числа для удобства. Также создадим массив visited
такого же размера и заведем счетчик островов, изначально равный 0.

Проходимся по всем элементам матрицы. Если элемент равен 1 и еще не был
посещен, значит это часть нового острова. Увеличиваем счетчик на 1 и добавляем
координаты элемента в очередь. Пока очерель не пуста, извлекаем из нее первый
элемент, помечаем его посещенным и смотрим на его соседей. Если сосед равен 1
и не помечен, то помечаем его и добавляем в очередь.

Лучшее решение: 247 ms, 20.15 Mb
#matrix #bfs
"""
from collections import deque


class Solution:

    def __make_frame(self, m: int, n: int, grid: list[list[str]]):
        new_grid = [[0] * (n + 2) for _ in range(m + 2)]
        for i in range(m):
            for j in range(n):
                new_grid[i + 1][j + 1] = int(grid[i][j])
        return new_grid

    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        grid = self.__make_frame(m, n, grid)
        visited = [[False] * (n + 2) for _ in range(m + 2)]
        shift_i = [0, -1, 0, 1]
        shift_j = [-1, 0, 1, 0]
        cnt = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if grid[i][j] and not visited[i][j]:
                    cnt += 1
                    q = deque([(i, j)])
                    visited[i][j] = True
                    while q:
                        curr_row, curr_col = q.popleft()
                        for k in range(4):
                            row = curr_row + shift_i[k]
                            col = curr_col + shift_j[k]
                            if grid[row][col] and not visited[row][col]:
                                q.append((row, col))
                                visited[row][col] = True
        return cnt
