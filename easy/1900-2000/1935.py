"""
Maximum Number of Words You Can Type.

Найти кол-во слов в тексте, не содержащих букв из набора brokenLetters.

Разбиваем исходный текст по пробелам и проверяем каждое слово.

Лучшее решение: 2 ms, 17.87 Mb
#hash_table #string
"""


class Solution:

    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        return sum(all(e not in broken for e in word) for word in text.split())
