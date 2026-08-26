"""
Find the Highest Altitude.

Велосипедист движется по маршруту из n + 1 точки. Он начинает движение в точке
0 на высоте 0. Дан массив целых чисел gain, gain[i] - перепад высоты между
точками i и i + 1. Найти наибольшую высоту точки на маршруте.

Устанавливаем текущее значение на 0 и последовательно прибавляем следующие
значения, обновляя максимум.

Лучшее решение: 0 ms (100%), 19.05 Mb (97.80%)
#array #prefix_sum
"""


class Solution:

    def largestAltitude(self, gain: list[int]) -> int:
        ans = 0
        curr = 0
        for e in gain:
            curr += e
            if curr > ans:
                ans = curr
        return ans
