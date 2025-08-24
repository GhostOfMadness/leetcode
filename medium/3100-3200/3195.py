"""
Find the Minimum Area to Cover All Ones I.

Найти минимальную площадь прямоугольника, который покрывает все единицы
в бинарной матрице размера m * n.

Для нахождения площади прямоугольника нужно знать его ширину и высоту. Для
ширины заведем переменные left и right, для высоты - up и down. Тогда площадь
будет равна (right + 1 - left) * (down + 1 - up).

Проходимся по каждой строке и ищем индексы первого и последнего вхождения
единицы в строку (curr_left, curr_right). Первая найденная единица фиксирует
текущую левую границу, любая найденная единица сдвигает правую границу. Если
найденный отрезок [curr_left, curr_right] не полностью лежит в [left, right],
то сдвигаем глобальные границы ширины. Первая строка, на которой оказались
единицы фиксирует границу up, каждая последующая строка с единицами сдвигает
down до текущей строки.

Лучшее решение: 2597 ms, 47.32 Mb
"""


class Solution:

    def minimumArea3(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        left = None
        right = None
        up = None
        down = None
        for r in range(m):
            curr_left, curr_right = None, None
            for c in range(n):
                if grid[r][c] == 1:
                    if curr_left is None:
                        curr_left = c
                    curr_right = c
            if left is None:
                left, right = curr_left, curr_right
            elif curr_left is not None:
                left = min(left, curr_left)
                right = max(right, curr_right)
            if curr_left is not None:
                if up is None:
                    up = r
                down = r
        return (right + 1 - left) * (down + 1 - up)
