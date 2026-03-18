"""
Check if Binary String Has at Most One Segment of Ones.

Дана бинарная строка s, которая начинается с единицы. Проверить, что в строке
ровно один блок из единиц.

Так как строка начинается с единицы, то единственный блок из единиц должен
быть в самом начале, поэтому считаем единицы, стартуя с индекса 0 = cnt_one.
Затем считаем количество нулей после этого блока = cnt_zero. Если в строке
ровно один блок единиц, что сумма cnt_one и cnt_zero даст длину строки.

Лучшее решение: 0 ms, 19.19 Mb
#string
"""


class Solution:

    def checkOnesSegment(self, s: str) -> bool:
        cnt_one = 0
        i = 0
        length = len(s)
        while i < length and s[i] == '1':
            cnt_one += 1
            i += 1
        cnt_zero = 0
        while i < length and s[i] == '0':
            cnt_zero += 1
            i += 1
        return (cnt_one + cnt_zero) == length
