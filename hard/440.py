"""
K-th Smallest in Lexicographical Order.

Найти k-е число в массиве чисел [1, n], записанном в лексикографическом
порядке.

Лучшее решение: 0 ms, 18.02 Mb
"""


import random
import time


class Solution:

    def count_size_array(
        self,
        depth: int,
        start: int,
        compare_to: int,
        total: int,
        is_full: bool = False,
    ):
        if is_full:
            return [int('1' * depth)] * 10
        arr = [0] * 10
        for i in range(start, 10):
            if i < compare_to:
                arr[i] = int('1' * depth)
            if i > compare_to and depth > 1:
                arr[i] = int('1' * (depth - 1))
        arr[compare_to] = total - sum(arr)
        return arr

    def findKthNumber(self, n: int, k: int) -> int:
        ans = ''
        total = n
        sn = str(n)
        depth = len(sn)
        while k > 0:
            compare_to = int(sn[len(sn) - depth])
            arr = self.count_size_array(
                depth=depth,
                start=int(not ans),
                compare_to=compare_to,
                total=total,
                is_full=(ans and not sn.startswith(ans)),
            )
            acc = 0
            for i in range(10):
                acc += arr[i]
                if acc >= k:
                    break
            ans += str(i)
            k = k - (acc - arr[i]) - 1
            if i != compare_to:
                depth = len(str(arr[i])) - 1
            else:
                depth -= 1
            total = arr[i] - 1
        return int(ans)

    def slow_algo(self, n: int, k: int) -> int:
        arr = sorted(range(1, n + 1), key=lambda e: str(e))
        return arr[k - 1]

    def test(self, slow_f, fast_f, n_iter: int = 10000):
        acc = 0
        for _ in range(n_iter):
            n = random.randint(1, 10000)
            k = random.randint(1, n)
            slow_ans = slow_f(n=n, k=k)
            fast_ans = fast_f(n=n, k=k)
            if slow_ans == fast_ans:
                acc += 1
            else:
                print(f'n = {n}, k = {k}')
                print(f'Верный ответ = {slow_ans}')
                print(f'Ответ быстрого алгоритма = {fast_ans}')
                break
        print(f'Успешно пройдено {acc} из {n_iter} тестов')

    def time_test(self, func, **params):
        start = time.perf_counter()
        func(**params)
        end = time.perf_counter()
        print(f'Время работы = {end - start:.5f} сек')
