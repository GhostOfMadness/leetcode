"""
Power of Four.

Необходимо определить является ли число n степенью 4.

Можно в цикле наращивать переменную curr, пока она не станет больше или равна
n, затем вернуть curr == n. Можно использовать биты числа. 4 - степень 2,
значит как и в случае с двойкой n & (n - 1) == 0. При этом общее количество
бит в записи степени 4 нечетное.

Лучшее решение: 0 ms, 17.61 Mb (17.79 Mb для битового решения)
"""


class Solution:

    def isPowerOfFour(self, n: int) -> bool:
        curr = 1
        while curr < n:
            curr <<= 2
        return curr == n

    def isPowerOfFour_bit(self, n: int) -> bool:
        return n & (n - 1) == 0 and n.bit_length() % 2 == 1
