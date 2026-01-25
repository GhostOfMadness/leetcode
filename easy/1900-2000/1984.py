"""
Minimum Difference Between Highest and Lowest of K Scores.

Дан массив целых неотрицательных чисел, из которого необходимо выбрать k
значений таким образом, чтобы разница между наибольшим и наименьшим числом
была минимальна.

Сортируем массив по возрастанию и идем по нему окном размера k, на каждом
шаге считая разность значений между концом и началом отрезка.

Лучшее решение: 0 ms, 19.55 Mb
#sorting #array #sliding_window
"""


class Solution:

    def minimumDifference(self, nums: list[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        return min(nums[i + k - 1] - nums[i] for i in range(n - k + 1))
