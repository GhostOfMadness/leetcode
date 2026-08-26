"""
Concatenate Non-Zero Digits and Multiply by Sum I.

Дано целое неотрицательное число n. x - число, полученное конкатенацией всех
ненулевых цифр числа n, а digitSum - сумма цифр в числе x. Найти произведение
x * digitSum.

Используем симуляцию процесса. Для этого число можно перевести в строку и
последовательно проходить слева направо или каждый раз выкидывать из числа
последнюю цифру, пока n не станет нулем, и работать сразу с числовым типом.
По времени работы на случайных тестах заметной разницы нет.

Лучшее решение: 0 ms (100%), 19.22 Mb (51.25%)
#math
"""


class Solution:

    def sumAndMultiplyStr(self, n: int) -> int:
        x = 0
        digitSum = 0
        for e in str(n):
            digit = int(e)
            if digit:
                x = x * 10 + digit
                digitSum += digit
        return x * digitSum

    def sumAndMultiplyMath(self, n: int) -> int:
        x = 0
        digitSum = 0
        size = 1
        while n:
            digit = n % 10
            if digit:
                digitSum += digit
                x = digit * size + x
                size *= 10
            n //= 10
        return x * digitSum
