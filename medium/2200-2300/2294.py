"""
Partition Array Such That Maximum Difference is K.

Найти наименьшее кол-во подмассивов, на которые можно разбить исходный
массив таким образом, чтобы максимальная разность элементов не превышала k.

Лучшее решение: 80 ms, 29.05 Mb
"""


class Solution:

    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        ans = 0
        prev = nums[0]
        for e in nums:
            if e - prev > k:
                ans += 1
                prev = e
        ans += 1
        return ans
