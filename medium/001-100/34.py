"""
Find First and Last Position of Element in Sorted Array.

Найти первое и последнее вхождение заданного элемента в отсортированный
массив целых чисел. Если такого числа нет, то вернуть [-1, -1].

Испоьзуем бинарный поиск. Сначала ищем индекс первого числа, которое строго
больше заданного. Если такого числа нет (поиск вернул 0 в качестве ответа)
или числа на позиции перед найденной не равно таргету, то искомого числа
просто нет в массиве и возвращаем -1. В ином случае, границей справа будет
найденная позиция за минусом 1. Второй бинарный поиск запускаем от начала
массива до найденной правой границы включительно и получаем левую границу
интервала.

Лучшее решение: 0 ms, 18.17 Mb
#binary_seacrh #array
"""


class Solution:

    def binSeacrhRight(self, nums: list[int], target: int, right: int) -> int:
        left = 0
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return right

    def binSearchLeft(self, nums: list[int], target: int, right: int) -> int:
        left = 0
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return right

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        length = len(nums)
        right = self.binSeacrhRight(nums, target, length)
        if not right or nums[right - 1] != target:
            return [-1, -1]
        right -= 1
        left = self.binSearchLeft(nums, target, right)
        return [left, right]
