"""
Maximum Difference by Remapping a Digit.

Числа a и b получаются заменой всех вхождений какой-либо цифры исходного
числа на любую другую цифру (полученное число может содержать ведущие нули).
Найти максимальную разницу abs(a - b).

Лучшее решение: 0 ms, 17.66 Mb
"""


class Solution:

    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        i = 0
        while i < len(s) and s[i] == '9':
            i += 1
        if i == len(s):
            return num
        return int(s.replace(s[i], '9')) - int(s.replace(s[0], '0'))
