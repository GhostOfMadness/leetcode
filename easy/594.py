"""
Longest Harmonious Subsequence.

Найти максимальную длину подпоследовательности, в которой максимальный
и минимальный элементы отличаются на 1.

Лучшее решение: 27 ms, 19.37 Mb
"""


from collections import Counter


class Solution:

    def findLHS(self, nums: list[int]) -> int:
        c = Counter(nums)
        skeys = sorted(c)
        return max(
            (
                c[skeys[i]] + c[skeys[i - 1]]
                for i in range(1, len(skeys))
                if skeys[i] - skeys[i - 1] == 1
            ),
            default=0,
        )
