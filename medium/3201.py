"""
Find the Maximum Length of Valid Subsequence I.

Найти максимальную длину подпоследовательности, в которой остаток от деления
каждых двух подряд идущих элементов на 2 одинаковый.

Такая подпоследовательность должна состоять только из четных или нечетных
чисел, или из них обоих с чередованием. Находим максимальную длину каждого
из этих 3 вариантов и выбираем максимум.

Лучшее решение: 69 ms, 39.09 Mb
"""


class Solution:

    def maximumLength(self, nums: list[int]) -> int:
        size = len(nums)
        odd_ans = sum(nums[i] & 1 for i in range(size))
        return max(
            odd_ans,
            size - odd_ans,
            1 + sum(nums[i] & 1 != nums[i - 1] & 1 for i in range(1, size))
        )
