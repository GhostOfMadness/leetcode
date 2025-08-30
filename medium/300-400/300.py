"""
Longest Increasing Subsequence.

Найти наибольшую длину возрастающего подмасссива, который получается путем
удаления некоторых элементов исходного массива без изменения порядка
следования оставшихся значений.

Используем динамическое программирование. От текущей позиции идет в начало
массива и смотрим на элемент nums[j]. Если он меньше nums[i], то dp[i] =
max(dp[i], dp[j] + 1). Ответом будет максимум в массиве dp.

Лучшее решение: 912 ms, 18.23 Mb
"""


class Solution:

    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1] * n
        ans = 1
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
            if dp[i] > ans:
                ans = dp[i]
        return ans
