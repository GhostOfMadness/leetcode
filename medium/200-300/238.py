"""
Product of Array Except Self.

Дан массив целых чисел nums. Необходимо вернуть массив такой же длины answer,
где answer[i] - произведение всех чисел, кроме nums[i].

Каждое значение формируется как произведение префикса и суффикса. Сначала
в answer занесем все префиксные произведения. Затем установим значение
суффикса на последний элемент в массиве (длина массива не меньше 2, поэтому
это точно можно сделать) и пойдем справа налево, умножая имеющийся префикс
на текущий суффикс и увеличивая значение суффикса.

Лучшее решение: 25 ms, 23.31 Mb
"""


class Solution:

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]
        suffix = nums[n - 1]
        for i in range(n - 2, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer
