"""
Find Subsequence of Length k With the Largest Sum.

Найти подпоследовательность чисел их исходного массива, которая дает
наибольшую сумму.

Лучшее решение: 3 ms, 17.92 Mb
"""


class Solution:

    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        return [
            e[1]
            for e in sorted(
                sorted(enumerate(nums), key=lambda x: x[1], reverse=True)[:k]
            )
        ]
