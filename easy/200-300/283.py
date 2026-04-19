"""
Move Zeroes.

Дан массив целых чисел nums. Необходимо переместить все нули в нем в конец,
сохранив при этом порядок ненулвых элементов.

Идем по массиву слева направо. Если нашли 0, то увеличиваем счетчик нулей
zero_cnt на 1. Если нашли ненулевой элемент, то меняем его значение с элементом
на позиции i - zero_cnt.

Лучшее решение: 4 ms, 20.52 Mb
#array
"""


class Solution:

    def moveZeroes(self, nums: list[int]) -> None:
        zero_cnt = 0
        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                zero_cnt += 1
            else:
                idx = i - zero_cnt
                nums[idx], nums[i] = nums[i], nums[idx]
