"""
Maximum Difference Between Even and Odd Frequency I.

Найти максимальную разность между нечетной и четной частотами символов.

Лучшее решение: 0 ms, 17.80 Mb
"""


import random
import time

from collections import Counter
from string import ascii_lowercase as letters


class Solution:

    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        return (
            max(e for e in c.values() if e % 2 != 0)
            - min(e for e in c.values() if e % 2 == 0)
        )

    def time_test(self):
        size = 10 ** 8
        s = random.choices(letters, k=size)
        start = time.perf_counter()
        self.maxDifference(s=s)
        end = time.perf_counter()
        print(f'Время работы = {end - start:.5f} сек')
