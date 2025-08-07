"""
Single Number.

Все числа массива, кроме одного, повторяются 2 раза. Найти число, которое
встречается только 1 раз.

Последовательно применим XOR к массиву. Каждая одинаковая пара чисел даст
0 и останется только одиночный элемент.

Лучшее решение: 0 ms, 19.54 Mb
"""


from functools import reduce


class Solution:

    def singleNumber(self, nums: list[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
