"""
Maximum Possible Number by Binary Concatenation.

Дан массив nums, состоящий из 3 целых чисел в диапазоне от 1 до 127. Найти
наибольшее число, которое может быть получено конкатенацией бинарной записи
данных чисел.

В массиве всего 3 числа, значит есть только 6 вариантов значений. Перебираем
каждый из них и выбираем максимум. Текущий ответ для каждой комбинации равен
0. Для каждого элемента сначала сдвигаем ответ на количество бит в текущем
числе, а затем делаем OR с этим числом, то есть прибавляем его в конец,
имитируя конкатенацию.

Лучшее решение: 0 ms, 19.30 Mb
#bit_manipulation #array #enumeration
"""
from itertools import permutations


class Solution:

    def maxGoodNumber(self, nums: list[int]) -> int:
        res = 0
        perms = permutations(nums)
        for perm in perms:
            ans = 0
            for e in perm:
                ans = (ans << e.bit_length()) | e
            if ans > res:
                res = ans
        return res
