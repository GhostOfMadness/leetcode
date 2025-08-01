"""
Lexicographical Numbers.

Сгенерировать последовательность чисел от 1 до n в лексикографическом порядке.

Лучшее решение: 3 ms, 24.14 Mb
"""


class Solution:

    def lexicalOrder(self, n: int) -> list[int]:
        return sorted(range(1, n + 1), key=lambda e: str(e))
