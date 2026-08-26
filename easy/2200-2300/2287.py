"""
Rearrange Characters to Make Target String.

Дана строка s и целевая строка target, состоящие из строчных латинских букв.
Определить сколько раз можно получить целевую строку из букв исходной строки
при условии, что каждую букву можно использовать один раз.

Сначала находим частоту каждой буквы в целевой строке, затем считаем частоту
этих букв в строке s. В качестве ответа берем минимум от целочисленного деления
частоты буквы в s на частоту в target, чтобы учесть, что буквы могут
использоваться в целевой строке любое количество раз.

Лучшее решение: 0 ms (100%), 19.25 Mb (74.13%)
#string #hash_table #counting
"""
from collections import Counter


class Solution:

    def rearrangeCharacters(self, s: str, target: str) -> int:
        targetMap = Counter(target)
        c = {letter: 0 for letter in targetMap}
        for letter in s:
            if letter in targetMap:
                c[letter] += 1
        return min(
            c[letter] // targetMap[letter] for letter in targetMap
        )
