"""
Sort Colors.

Отсортировать массив, состоящий из цифр 0, 1, 2 в порядке возрастания, не
используя встроенную сортировку.

Реализуем алгоритм быстрой сортировки с единицей в качестве опорного элемента.
less указывает на положение последнего нуля, equal - на положение последней
единицы. Оба указателя изначально стоят на -1.

Если новый элемент равен опорному, то его нужно добавить справа от позиции
euqal, то есть на equal + 1. Для этого делаем swap nums[i] и nums[equal + 1]
и сдвигаем equal на 1. Такой подход сработает неправильно, если найденная
единица - первая в массиве, а до этого был хотя был 1 ноль. В этом случае
найденную единицу нужно переместить на позицию less + 1.

Если новый элемент меньше опорного, то меняем его с элементом на позиции
less + 1 и сдвигаем less на 1. Если указатель equal не равен -1, то на позицию
i мы перекинули единицу, которую теперь нужно переставить на equal + 1 и
сдвинуть equal на 1.

Лучшее решение: 0 ms, 17.68 Mb
"""


class Solution:

    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        less, equal = -1, -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if less != -1 and equal == -1:
                    nums[i], nums[less + 1] = nums[less + 1], nums[i]
                    equal = less + 1
                else:
                    nums[i], nums[equal + 1] = nums[equal + 1], nums[i]
                    equal += 1
            elif nums[i] < 1:
                nums[i], nums[less + 1] = nums[less + 1], nums[i]
                less += 1
                if equal != -1:
                    nums[i], nums[equal + 1] = nums[equal + 1], nums[i]
                    equal += 1
