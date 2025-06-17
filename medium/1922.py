"""
Count Good Numbers.

Необходимо найти количество строк длины n, где на четных позициях стоят
четные цифры (на 0-1 позиции может стоят 0), а на нечетных - простые.

Лучшее решение: 0 ms, 17.79 Mb
"""


class Solution:

    mod: int = 10 ** 9 + 7

    def __exponentiation(self, val: int, degree: int) -> int:
        bits = bin(degree)[2:]
        ans = 1
        for bit in bits:
            ans = ((ans ** 2) % self.mod * val ** int(bit)) % self.mod
        return ans

    def countGoodNumbers(self, n: int) -> int:
        odd_cnt = n // 2
        even_cnt = n - odd_cnt
        return (
            self.__exponentiation(5, even_cnt)
            * self.__exponentiation(4, odd_cnt)
        ) % self.mod


if __name__ == '__main__':
    res = Solution()
    n = 10 ** 15
    print(res.countGoodNumbers(n=n))
