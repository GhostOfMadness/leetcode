"""
Binary Number With Alternating Bits.

Задано целое положительное число n в пределах 32 бит. Вернуть True, если в нем
нет двух одинаковых подряд идущих битов, иначе - False.

Можно идти слева направо и проверять текущий бит с сохраненным предыдущим.
Если они равны, то возвращаем False. Если цикл дошел до конца, то число
подходит под условие, поэтому возвращем True. Можно найти количество бит
в исходном числе и на основе этого найти число, которое соответствует условию,
и сравнить его с n. На моих тестах этот вариант работает в 3 раза медленнее
(возможно из-за того, что в первом случае есть ранняя остановка).

Лучшее решение: 0 ms, 19.30 Mb
#bit_manipulation
"""


class Solution:

    def hasAlternatingBits(self, n: int) -> bool:
        deg = 1
        prev = -1
        while deg < n:
            curr = n & deg
            if curr > 0 and prev > 0 or prev == curr == 0:
                return False
            prev = curr
            deg <<= 1
        return True

    def hasAlternatingBits2(self, n: int) -> bool:
        length = n.bit_length()
        num = 0
        steps = (length + 1) >> 1
        if length & 1:
            deg = 1
        else:
            deg = 2
        for _ in range(steps):
            num += deg
            deg <<= 2
        return num == n
