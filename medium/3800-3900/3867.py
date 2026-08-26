"""
Sum of GCD of Formed Pairs.

Дан массиы целых положительных чисел nums. Необходимо выполнить следующие
действия:
1. Найти массив prefixGcd, prefixGcd[i] = gcd(nums[i], max(nums[0...i])),
   т.е. это наибольший общий делитель для i-го числа и максимума на префиксе
   nums[:i + 1].
2. Отсортировать массив prefixGcd по возрастанию.
3. Сформировать пары из наименьшего и наибольшего еще неиспользованного
   значения, найти GCD для каждой такой пары.
4. В качестве ответа вернуть сумму найденных GCD.

Используем симуляцию процесса.

Лучшее решение: 163 ms (89.22%) 33.66 Mb (55.09%)
#math #simulation #array
"""
from math import gcd


class Solution:

    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = [0] * n
        prefixGcd[0] = nums[0]
        currMax = nums[0]
        for i in range(1, n):
            num = nums[i]
            if num >= currMax:
                prefixGcd[i] = num
                currMax = num
            else:
                prefixGcd[i] = gcd(num, currMax)
        prefixGcd.sort()
        return sum(
            gcd(prefixGcd[j], prefixGcd[n - j - 1])
            for j in range(n // 2)
        )