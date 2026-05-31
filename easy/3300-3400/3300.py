"""
Minimum Element After Replacement With Digit Sum

Дан массив целых положительных чисел nums. К каждому числу применяется
операция, преобразующая его в сумму его цифр. Найти минимум из полученных
значений.

Используем симуляцию процесса. Можно преобразовать каждое число в строку,
затем применить int() к каждой цифре и найти сумму. А можно последовательно
делить число на 10, суммируя остатки от этого деления, пока число не станет
нулем. Второй вариант работает быстрее.

Лучшее решение: 1 ms (87.03%), 19.45 Mb (21.61%)
#math #array
"""


class Solution:

    def minElement(self, nums: list[int]) -> int:
        ans = float('inf')
        for num in nums:
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num //= 10
            if digit_sum < ans:
                ans = digit_sum
        return ans
