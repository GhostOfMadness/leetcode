"""
Power of Three.

Необходимо проверить является ли число степенью 3.

В цикле наращиваем переменную curr, пока она не станет больше или равна n.
Возвращаем результат n == curr. Или можно проверить, что число является
положительным и 3 ** 19 делится на него без остатка. 3 ** 19 - максимальная
степень 3 в 32 битах.

Лучшее решение: 5 ms, 17.68 Mb
"""
from test_class import Test


class Solution(Test):

    def isPowerOfThree(self, n: int) -> bool:
        curr = 1
        while curr < n:
            curr *= 3
        return curr == n

    def isPowerOfThree2(self, n: int) -> bool:
        return n > 0 and 3 ** 19 % n == 0
