"""
Find Most Frequent Vowel and Conconant.

Найти найти наиболее часто встречающуюся гласную и согласную в строке
и суммировать их частоты.

Считаем частоты каждой буквы в строке. С помощью функции max находим
максимальную частоту гласной и согласной и складываем их.

Лучшее решение: 0 ms, 17.70 Mb
#string #counting #hash_table
"""
from collections import Counter


class Solution:

    def maxFreqSum(self, s: str) -> int:
        c = Counter(s)
        return (
            max((v for k, v in c.items() if k in 'aeiou'), default=0)
            + max((v for k, v in c.items() if k not in 'aeiou'), default=0)
        )
