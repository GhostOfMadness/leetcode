"""
Maximum Unique Subarray Sum After Deletion.

Найти максимальную сумму элементов массива после удаления любого количества
исходных значений. Массив не должен стать пустым, все значения в массиве
должны быть уникальными.

Если максимальное значение массива меньше или равно 0, то возвращаем его,
иначе - сумму всех уникальных положительных чисел.
"""


class Solution:

    def maxSum(self, nums: list[int]) -> int:
        max_val = max(nums)
        if max_val <= 0:
            return max_val
        return sum(set(e for e in nums if e > 0))
