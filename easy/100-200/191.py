"""
Number of 1 Bits.

Найти количество единичных битов в двоичной записи числа n.

Функция bit_count() как раз считает это значение.

Лучшее решение: 0 ms, 17.72 Mb
"""


class Solution:

    def hammingWeight(self, n: int) -> int:
        return n.bit_count()
