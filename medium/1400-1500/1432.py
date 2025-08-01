"""
Max Difference You Can Get From Changing an Integer.

Числа a и b получаются заменой всех вхождений какой-либо цифры исходного
числа на любую другую цифру. Найти максимальное значение abs(a - b).

Лучшее решение: 0 ms, 17.73 Mb
"""


class Solution:

    def max_value(self, num: str) -> int:
        i = 0
        n = len(num)
        while i < n and num[i] == '9':
            i += 1
        if i == n:
            return int(num)
        return int(num.replace(num[i], '9'))

    def min_value(self, num: str) -> int:
        i = 0
        n = len(num)
        while i < n and num[i] in {'0', '1'}:
            i += 1
        if i == 0:
            return int(num.replace(num[i], '1'))
        if i == n:
            return int(num)
        return int(num.replace(num[i], '0'))

    def maxDiff(self, num: int) -> int:
        return self.max_value(str(num)) - self.min_value(str(num))
