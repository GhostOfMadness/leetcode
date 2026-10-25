"""
Circle and Rectangle Overlapping.

Даны центр и радиус круга и координаты левого нижнего и правого верхнего угла
прямоугольника. Определить, пересекаются ли круг и прямоугольник на плоскости.

Центр окружности точно должен лежать в границах внешнего прямоугольника,
стороны которого отступают на radius от сторон исходного прямоугольника. Но
углы это внешнего прямоугольника не прямые, а представляют собой дуги
окружностей радиуса radius, центры этих окружностей расположены в углах
исходного прямоугольника. Таким образом, нужно проверить, что центр окружности
лежит в границах внешнего "прямоугольника", а если этот центр не лежит напротив
одной из сторон исходного прямоугольника, то добавить проверку на вхождение
в окружность с центром в нужном углу прямоугольника.

Лучшее решение: 0 ms (100%), 19.44 Mb (18.67%)
#math #geometry
"""


class Solution:

    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        out_x1, out_x2 = x1 - radius, x2 + radius
        out_y1, out_y2 = y1 - radius, y2 + radius
        tl_eq = (x1 - xCenter) ** 2 + (y2 - yCenter) ** 2 <= radius ** 2
        tr_eq = (x2 - xCenter) ** 2 + (y2 - yCenter) ** 2 <= radius ** 2
        br_eq = (x2 - xCenter) ** 2 + (y1 - yCenter) ** 2 <= radius ** 2
        bl_eq = (x1 - xCenter) ** 2 + (y1 - yCenter) ** 2 <= radius ** 2
        cond = (
            not (out_x1 <= xCenter <= out_x2 and out_y1 <= yCenter <= out_y2)
            or (xCenter < x1 and yCenter > y2 and not tl_eq)
            or (xCenter > x2 and yCenter > y2 and not tr_eq)
            or (xCenter > x2 and yCenter < y1 and not br_eq)
            or (xCenter < x1 and yCenter < y1 and not bl_eq)
        )
        return not cond
