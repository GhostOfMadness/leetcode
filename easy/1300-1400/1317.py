"""
Convert Integer to the Sum of Two No-Zero Integers.

Разложить число на сумму двух целых чисел, не содержащих 0 в записи.

Перебираем все варианты пар чисел и проверяем их на наличие 0.

Лучшее решение: 0 ms, 17.69 Mb
#math
"""


class Solution:

    def getNoZeroIntegers(self, n: int) -> list[int]:
        for i in range(1, n // 2 + 1):
            sec = n - i
            if str(sec).find('0') == -1 and str(i).find('0') == -1:
                return [sec, i]
