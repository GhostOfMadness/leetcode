"""
Search Insert Position.

Дан отсортированный список уникальных целых чисел. Найти индекс заданного
числа в списке, если оно там есть, или индекс, на который это число нужно
поместить, чтобы не нарушить сортировку.

С помощью бинарного поиска находим индекс первого числа, которое больше
заданного (переменная right). Если число перед ним равно заданному, то
возращаем его индекс, то есть right - 1, иначе - right, так как число на
позиции right - 1 точно меньше, а на right - точно больше.

Лучшее решение: 0 ms, 18.18 Mb
#binary_seacrh #array
"""


class Solution:

    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        if nums[right - 1] == target:
            return right - 1
        return right
