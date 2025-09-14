"""
Find N Unique Integers Sum up to Zero.

Вывести массив из N любых уникальных целых чисел, которые в сумме дают 0.

half = N // 2. Возьмем half пар чисел, каждая из которых в сумме дает 0.
Например, если N = 6, то half = 3, то есть нужны 3 пары чисел: [-1, 1],
[2, -2], [3, -3]. Если N четное, то это этих пар достаточно, если нечетное,
то к ним еще добавляется 0.

Лучшее решение: 0 ms, 17.78 Mb
#math #array
"""


class Solution:

    def sumZero(self, n: int) -> list[int]:
        half = n // 2
        if n % 2:
            return list(range(-half, half + 1))
        return list(range(-half, 0)) + list(range(1, half + 1))


if __name__ == '__main__':
    res = Solution()
    print(res.sumZero(7))
