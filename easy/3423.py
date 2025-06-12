"""
Maximum Difference Between Adjacent Elements in a Circular Array.

Найти наибольшую абсолютную разницу соседних элементов в кольцевом массиве.

Лучшее решение: 1 ms, 17.61 Mb
"""


class Solution:

    def maxAdjacentDistance(self, nums: list[int]) -> int:
        n = len(nums)
        max_val = max(abs(nums[i] - nums[i + 1]) for i in range(n - 1))
        return max(max_val, abs(nums[n - 1] - nums[0]))
