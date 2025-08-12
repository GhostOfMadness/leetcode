"""
Reordered Power of 2.

Дано число из отрезка [1, 10 ** 9]. Необходимо сказать, является ли какая-либо
перестановка из его цифр степенью двойки.

Переведем исходное число в строчку и посчитаем частоту вхождения его цифр.
Затем определим минимальное число, которое может быть получено при
перестановке цифр с учетом того, что в начале не может стоять ноль (то есть
кол-во разрядов не меняется). Установим curr на 1, это текущая степень двойки
и будем сдвигать до тех пор, пока он меньше минимального числа. После этого,
для каждой степени двойки нужной разрядности находим словарь частот
и сравниваем его со словарем исходного числа. Если есть совпадение, то
возвращаем True, иначе - False.

Лучшее решение: 0 ms, 17.77 Mb
"""
from collections import Counter


class Solution:

    def reorderedPowerOf2(self, n: int) -> bool:
        num = str(n)
        curr_set = Counter(num)
        min_digit = min(e for e in num if e != '0')
        min_idx = num.find(min_digit)
        low_border = int(
            min_digit
            + ''.join(sorted(num[:min_idx] + num[min_idx + 1:]))
        )
        total = curr_set.total()
        curr = 1
        while curr < low_border:
            curr <<= 1
        while len(str(curr)) == total:
            c = Counter(str(curr))
            if c == curr_set:
                return True
            curr <<= 1
        return False
