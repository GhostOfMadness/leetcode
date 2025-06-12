"""
Distribute Candies Among Children II.

Найти количество способов распределить n конфет так, чтобы каждый из 3-х
детей получил не больше, чем limit конфет.

Лучшее решение: 1099 ms, 17.88 Mb
"""


class Solution:

    def distributeCandies(self, n: int, limit: int) -> int:
        acc = 0
        for i in range(min(n, limit) + 1):
            left = n - i
            if left <= limit:
                acc += left + 1
            elif limit < left <= 2 * limit:
                acc += 2 * limit - left + 1
        return acc
