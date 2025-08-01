"""
Minimum Number of Operations to Satisfy Conditions.

Необходимо найти минимальное количество операций, за которое можно
преобразовать исходную матрицу так, чтобы:
- все числа внутри одного столбца совпадали;
- числа в текущем столбце не совпадали с правым соседом (если есть).

Лучшее решение: 179 ms, 54.43 Mb
"""


from collections import Counter


class Solution:

    def get_count_array(self, col_num, grid, n):
        c = Counter(row[col_num] for row in grid)
        return [n if i not in c else n - c[i] for i in range(10)]

    def get_two_mins(self, arr: list[int]):
        first_min = float('inf')
        first_min_idx = None
        second_min = float('inf')
        second_min_idx = None
        for i in range(len(arr)):
            if arr[i] < first_min:
                second_min = first_min
                second_min_idx = first_min_idx
                first_min = arr[i]
                first_min_idx = i
            elif arr[i] < second_min:
                second_min = arr[i]
                second_min_idx = i
        return first_min_idx, second_min_idx

    def minimumOperations(self, grid: list[list[int]]) -> int:
        n = len(grid)
        prev = self.get_count_array(col_num=0, grid=grid, n=n)
        first_min, second_min = self.get_two_mins(arr=prev)
        for col in range(1, len(grid[0])):
            curr = self.get_count_array(col_num=col, grid=grid, n=n)
            for i in range(10):
                if i != first_min:
                    curr[i] += prev[first_min]
                else:
                    curr[i] += prev[second_min]
            prev = curr
            first_min, second_min = self.get_two_mins(arr=prev)
        return min(prev)
