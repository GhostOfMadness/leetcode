"""
Transformed Array.

Дан кольцевой массив целых чисел nums. Необходимо составить массив result
такого же размера по следующим правилам:
- если nums[i] > 0, то движемся от i на nums[i] элементов вправо, в result[i]
  заносим значение, на котором остановились.
- если nums[i] == 0, то result[i] == nums[i].
- если nums[i] < 0, то движемся от i на abs(nums[i]) шагов влево, в result[i]
  заносим значение, на котором остановились.

Так как массив кольцевой, то остановка при движении вправо определяется как
(i + nums[i]) % length. Эта же формула работает и при движении влево с
получением отрицательных чисел (остаток от целочисленного деления
положительный).

Лучшее решение: 51 ms, 19.30 Mb
#array #simulation
"""


class Solution:

    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        length = len(nums)
        return [nums[(i + nums[i]) % length] for i in range(length)]
