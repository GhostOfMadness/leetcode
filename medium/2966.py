"""
Divide Array Into Arrays With Max Difference.

Разделить исходный массив на подмассивы размера 3 так, чтобы максимальная
разница между элементами подмассива не превышала k.

Лучшее решение: 79 ms, 33.40 Mb
"""


class Solution:

    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        ans = []
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k:
                return []
            ans.append(nums[i:i + 3])
        return ans
