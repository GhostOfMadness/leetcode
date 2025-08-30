"""
Valid Anagram.

Проверить, являются ли строка s анаграммой строки t.

Для этого проверяем равенство словарей частот для этих строк.

Лучшее решение: 7 ms, 17.74 Mb
"""
from collections import Counter as c


class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        return c(s) == c(t)
