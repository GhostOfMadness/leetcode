"""
Minimum Absolute Difference.

Необходимо найти все пары чисел, модуль разности которых был бы равен
минимально возможному значению. Числа в массиве не повторяются.

Лучшее решение: 44 ms, 30.07 Mb
"""


class Solution:

    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        ans = []
        min_diff = float('inf')
        for i in range(len(arr) - 1):
            a = arr[i]
            b = arr[i + 1]
            diff = b - a
            if diff < min_diff:
                print('in if')
                min_diff = diff
                ans = []
            if diff == min_diff:
                ans.append([a, b])
        return ans


if __name__ == '__main__':
    res = Solution()
    arr = [4, 2, 1, 3]
    print(res.minimumAbsDifference(arr))
