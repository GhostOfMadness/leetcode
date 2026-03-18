"""
Sort Integers by The Number of 1 Bits.

Дан массив целых положительных чисел. Необходимо отсортировать его по
возрастанию количества установленных бит, если это число совпадает - по
возрастанию значения.

Используем встроенную сортировку по двум параметрам: количество единичных
битов (функция bit_count), само число.

Лучшее решение: 2 ms, 19.52 Mb
#array #sorting #bit_manipulation
"""


class Solution:

    def sortByBits(self, arr: list[int]) -> list[int]:
        arr.sort(key=lambda e: (e.bit_count(), e))
        return arr
