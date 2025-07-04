"""
Count Primes.

Посчитать количество простых чисел, которые строго меньше n.

Лучшее решение: 899 ms, 95.40 Mb
"""


class Solution:

    def countPrimes(self, n: int) -> int:
        nums = [1] * (n)
        for i in range(2, n):
            if i ** 2 >= n:
                break
            if nums[i]:
                step = i if i == 2 else 2 * i
                for j in range(i ** 2, n, step):
                    nums[j] = 0
        return sum(nums[2:])
