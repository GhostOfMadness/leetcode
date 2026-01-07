"""
Largest Triangle Area.

Дан массив точек на плоскости. Найти наибольшую площадь треугольника, который
можно получить используя три точки.

Пусть p1, p2, p3 - координаты точек, где pi = [xi, yi], тогда площадь равна
abs((p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])) / 2.
Перебираем все наборы точек, считаем полученную площадь и обновляем ответ.
Если точки находятся на одной прямой, то формула вернет 0.

Лучшее решение: 31 ms, 17.72 Mb
#math #geaometry
"""
from itertools import combinations


class Solution:

    def largestTriangleArea(self, points: list[list[int]]) -> float:
        ans = 0
        for p1, p2, p3 in combinations(points, 3):
            s = (
                abs(
                    (p2[0] - p1[0]) * (p3[1] - p1[1])
                    - (p3[0] - p1[0]) * (p2[1] - p1[1])
                )
                / 2
            )
            if s > ans:
                ans = s
        return round(ans, 5)
