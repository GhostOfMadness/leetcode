"""
Add binary.

Необходимо реализовать побитовое сложение двух чисел в двоичной записи,
заданных строками a и b.

Идем справа налево и складываем биты. В переменной buff храним перенос.
Возможны 3 ситуации:
- e1 = 0, e2 = 0. Если buff = 0, то в ответ пойдет 0, buff не поменяется. Если
  buff = 1, то в ответ идет 1, buff = 0.
- e1 = 1, e2 = 1. Если buff = 0, то в ответ идет 0, buff = 1. Если buff = 1,
  то в ответ идет 1, buff остается единицей.
- e1 = 0 и e2 = 1, e1 = 1 и e2 = 0. Если buff = 1, то в ответ идет 0, buff не
  меняется. Если buff = 0, то в ответ идет 1, buff не меняется.

Числа могут состоять из разного числа битов, поэтому недостающие значения в
строке меньшей длины можно дополнить нулями. Это и делает zip_longeset с
fillvalue = '0'. Функция возвращает итератор по паре строк.

Лучшее решение: 0 ms, 19.47 Mb
#bit_manipulation
"""
from itertools import zip_longest


class Solution:

    def addBinary(self, a: str, b: str) -> str:
        ans = []
        buff = 0
        for e1, e2 in zip_longest(a[::-1], b[::-1], fillvalue='0'):
            if e1 == e2 == '0':
                ans.append(buff)
                buff = 0
            elif e1 == e2 == '1':
                ans.append(buff)
                buff = 1
            else:
                if buff:
                    ans.append(0)
                else:
                    ans.append(1)
        if buff:
            ans.append(1)
        return ''.join(map(str, ans[::-1]))
