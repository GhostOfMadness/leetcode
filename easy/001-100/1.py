"""
Two Sum.

Вернуть индексы 2-х элементов массива, которые в сумме дают target.

Лучшее решение: 2 ms, 18.86 Mb
"""


class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ans = None
        d = dict()
        for idx, val in enumerate(nums):
            search = target - val
            if search in d:
                return [d[search], idx]
            d[val] = d.get(val, idx)
        return ans
