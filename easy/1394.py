"""
Find Lucky Integer in an Array.

Найти наибольшее число, частота которого в массиве совпадает с его значением.

Лучшее решение: 0 ms, 17.82 Mb
"""
from collections import Counter


class Solution:

    def findLucky(self, arr: list[int]) -> int:
        return max((k for k, v in Counter(arr).items() if k == v), default=-1)
