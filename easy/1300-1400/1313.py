"""
Decompress Run-Length Encoded List.

Дан массив четной длины nums, представляющий собой кодировку исходного массива.
Каждая пара чисел nums[2 * i], nums[2 * i + 1] (i >= 0) представляет собой
частоту и значение, которое с этой частотой входит в исходный массив. Нужно
восстановить исходный массив.

Используем симуляцию процесса. Идем по каждой соседней паре чисел и добавляем
значение с нужной частотой в результирующий массив.

Лучшее решение: 0 ms (100%), 19.44 Mb (17.27%)
#array
"""


class Solution:

    def decompressRLElist(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i + 1]
            ans.extend([val] * freq)
        return ans
