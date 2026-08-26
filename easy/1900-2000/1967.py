"""
Number of Strings That Appear as Substrings in Word.

Дан набор строк patterns и слово word. Найти количество строк из массива
patterns, которые есть в word.

Так размер массива и длины строк малы, то достаточно использовать встроенную
проверку вхождения для каждой строки массива.

Лучшее решение: 0 ms (100%), 19.28 Mb (58.44%)
#string
"""


class Solution:

    def numOfStrings(self, patterns: list[str], word: str) -> int:
        return sum(1 for pat in patterns if pat in word)
