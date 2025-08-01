"""
Count Special Integers.

Посчитать количество чисел на отрезке [1, n], состоящих из различных чисел.

Лучшее решение: 0 ms, 17.88 Mb
"""


class Solution:

    def slow_algo(self, n: int) -> int:
        return sum(len(set(str(e))) == len(str(e)) for e in range(1, n + 1))

    def countSpecialNumbers(self, n: int) -> int:
        if n < 10:
            return n

        sn = str(n)
        size = len(sn)
        base = 9
        prev = 9
        for i in range(size - 2):
            prev *= 9 - i
            base += prev

        dp = int(sn[0])
        is_special = True
        for i in range(1, size):
            if is_special:
                cnt = sum(1 for e in sn[:i] if int(e) <= int(sn[i]))
                dp = (dp - 1) * (10 - i) + int(sn[i]) + 1 - cnt
                is_special = len(set(sn[:i + 1])) == i + 1
            else:
                dp = dp * (10 - i)
        return base + dp

    def test(self):
        up = 10000
        acc = 0
        for num in range(1, up):
            ans = self.slow_algo(n=num)
            fans = self.countSpecialNumbers(n=num)
            if ans != fans:
                print(f'n = {num}')
                print(f'Правильный ответ = {ans}')
                print(f'Мой ответ = {fans}')
                break
            acc += 1
        print(f'Успешно проверены {acc} чисел от 1 до {up}')
