"""
Sort Matrix by Diagonals.

Отсортировать квадратную матрицу по диагоналям лево, верх - право, низ.
Диагонали в левом нижнем углу должны быть отсортированы по убыванию (включая
диагональ по row - col = 0), в правом верхнем углу - по возрастанию.

Первый вариант решения сначала сортирует диагонали левого нижнего угла
матрицы. Для этого на каждом шаге определяем начальные значения row и col,
затем собираем значения диагонали в массив arr, увеличивая row и col на 1.
Сортируем arr и заносим значения на диагональ. Затем делаем аналогичный
цикл для сортировки правого верхнего угла.

Во втором варианте решения итерируемся по разности, которая определяет
диагональ. Она находится в диапазоне от n - 1 до -(n - 1), при индексации
с 0. diff = row - col. Если diff положительная, то работает с нижним левым
углом, отрицательная - верхним правым. В случае левого нижнего угла каждая
диагональ начинается из 0-го столбца строки row, то есть row = diff. Чтобы
собрать эту диагональ в массив, необходимо спуститься от row до n, при этом
номер столбца определяется как row - diff. Сортируем полученный массив по
убыванию и заполняем диагональ как бы с конца, начиная от строки n - 1,
чтобы на каждом шаге брать последний элемент массива. Похожим образом
поступаем с правым верхним углом, только там не строка будет двигаться до n,
а столбец, начальное значение которого равно - diff.

Второй вариант компактнее, нет повторения кода, на моих тестах работал чуть
быстрее, но на платформе быстрее оказался 1-й вариант.

Лучшее решение 1: 4 ms, 17.88 Mb
Лучшее решение 2: 13 ms, 17.73 Mb
"""


class Solution:

    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        ans = [[0] * n for _ in range(n)]
        for row in range(n):
            curr = row
            col = 0
            arr = []
            while curr < n:
                arr.append(grid[curr][col])
                curr += 1
                col += 1
            arr.sort(reverse=True)
            col = 0
            i = 0
            while row < n:
                ans[row][col] = arr[i]
                row += 1
                col += 1
                i += 1
        for col in range(1, n):
            curr = col
            row = 0
            arr = []
            while curr < n:
                arr.append(grid[row][curr])
                row += 1
                curr += 1
            arr.sort()
            row = 0
            i = 0
            while col < n:
                ans[row][col] = arr[i]
                row += 1
                col += 1
                i += 1
        return ans

    def sortMatrix2(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        for diff in range(n - 1, -n, -1):
            if diff >= 0:
                arr = sorted(
                    [grid[r][r - diff] for r in range(diff, n)],
                    reverse=True,
                )
                for r in range(n - 1, diff - 1, -1):
                    grid[r][r - diff] = arr.pop()
            else:
                arr = sorted([grid[c + diff][c] for c in range(-diff, n)])
                for c in range(n - 1, -diff - 1, -1):
                    grid[c + diff][c] = arr.pop()
        return grid
