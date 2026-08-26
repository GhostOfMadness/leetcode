"""
Maximum Number of Balloons.

Дана строка text, состоящая из строчных латинских букв. Определить, сколько
раз можно составить слово 'balloon' из букв этой строки при условии, что
каджую букву можно использовать только 1 раз.

Считаем вхождение каждой буквы в строку. Ответом будет минимальное количество
вхождений букв 'balon'. Частота букв 'l' и 'o' при поиске ответа делится на
2 и округляется вниз, так как эти буквы используются в слове по 2 раза.

Лучшее решение: 0 ms (100%), 19.21 Mb (75.19%)
#string #hash_table #counting
"""
from collections import Counter


class Solution:

    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        return min(
            c.get('b', 0),
            c.get('a', 0),
            c.get('n', 0),
            c.get('l', 0) // 2,
            c.get('o', 0) // 2,
        )
