"""
Count Elements With Maximum Frequency.

Найти сумму частот элементов массива с наибольшей частотой.

Считаем частоту каждого элемента массива и находим максимальную. Проходимся
по всем частотам и суммируем максимальные.

Лучшее решение: 0 ms, 17.68 Mb
#array #hash_table #counting
"""
from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        arr = Counter(nums).values()
        max_freq = max(arr)
        return sum(max_freq for v in arr if v == max_freq)
