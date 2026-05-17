"""
Separate the Digits in an Array.

Дан массив целых положительных чисел nums. Необходимо разложить каждое число
на цифры, собрать все цифры в один массив и вернуть его. Цифры для каждого
числа идут в исходном порядке, то есть от старшего разряда к младшему.

Переводим каждое число в строку, формируем из него список цифр в формате int
и добавляем к ответу. Однако на случайных тестах быстрее работает вариант
с формированием единой строки из всех чисел с последующим переводом в список
цифр.

Лучшее решение: 3 ms (76.03%), 19.33 Mb (84.71%)
#array #simulation
"""


class Solution:

    def separateDigits(self, nums: list[int]) -> list[int]:
        return list(map(int, ''.join(map(str, nums))))

    def separateDigits2(self, nums: list[int]) -> list[int]:
        ans = []
        for num in nums:
            ans.extend(list(map(int, str(num))))
        return ans
