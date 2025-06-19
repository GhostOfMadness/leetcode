"""
Search a 2D Matrix.

Проверить, есть ли target в матрице, где каждая строка отсортирована по
неубыванию, а первый элемент текущей строки больше последнего элемента
предыдущей строки.

Лучшее решение: 0 ms, 18.19 Mb
"""


class Solution:

    def binary_search(self, arr: list[int], target: int):
        size = len(arr)
        left, right = 0, size
        mid = size // 2
        while left < right:
            if arr[mid] == target:
                return True
            if target < arr[mid]:
                right = mid
            if target > arr[mid]:
                left = mid + 1
            mid = (right + left) // 2
        return False

    def binary_search_col(self, matrix: list[list[int]], target: int):
        size = len(matrix)
        left, right = 0, size
        mid = (left + right) // 2
        while left < right:
            if matrix[mid][0] == target:
                return mid
            if target < matrix[mid][0]:
                right = mid
            if target > matrix[mid][0]:
                left = mid + 1
            mid = (left + right) // 2
        return mid - 1

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row = self.binary_search_col(matrix, target)
        return self.binary_search(matrix[row], target)
