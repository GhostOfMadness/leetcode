"""
Unique 3-Digit Even Numbers.

Дан массив цифр digits. Найти количество уникальных четных трехзначных чисел,
которые можно получить перестановкой цифр этого массива.

Используем brute force. Находим каждую уникальную комбинацию с помощью
permutations и set и проверяем ее на четность, а также смотрим, что она не
начинается с 0. Размер массива цифр маленький (не больше 10), поэтому
использование permutations имеет смысл.

Лучшее решение: 12 ms (76.04%), 19.27 Mb (72.53%)
#array #counting
"""
from itertools import permutations


class Solution:

    def totalNumbers(self, digits: list[int]) -> int:
        return sum(
            1
            for comb in set(permutations(digits, 3))
            if comb[2] & 1 == 0 and comb[0] != 0
        )
