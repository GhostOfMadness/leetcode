"""
Maximum Area of Longest Diagonal Reactangle.

Дан двумерный массив, каждое значение которого задает длину и ширину
прямоугольника. Найти площадь прямоугольника с наибольшей диагональю.
Если таким несколько, то вывести наибольшую площадь из них.

Длина диагонали ищется по формуле Пифагора (корень можно опустить). Если
полученная длина больше имеющейся, то обновляем длину диагонали и ответ.
Если длина диагонали равна имеющейся и площадь больше текущего ответа,
то обновляем ответ.

Лучшее решение: 0 ms, 17.80 Mb
"""


class Solution:

    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        curr_diag = 0
        ans = 0
        for h, w in dimensions:
            diag = h * h + w * w
            square = h * w
            if diag > curr_diag:
                curr_diag = diag
                ans = square
            elif diag == curr_diag and square > ans:
                ans = square
        return ans
