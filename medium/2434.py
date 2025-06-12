"""
Using a Robot to Print the Lexicographically Smallest String.

Дана исходная строка s и строка t, которая изначально пуста. На каждом шаге
можно выполнить одну из двух операций:
- Взять первый символ строки s и добавить его в конец t.
- Взять последний символ строки t и записать его в ответ.
Необходимо найти лексикграфически наименьшую строку, которая может быть
получена по этим правилам.

Лучшее решение: 370 ms, 21.72 Mb
"""


import random
import time

from collections import Counter, deque
from string import ascii_lowercase as letters


class Solution:

    def compare(self, letter: str, s: str) -> bool:
        return all(letter <= e for e in s)

    def slow_algo(self, s: str) -> str:
        t = []
        ans = ''
        i = 0
        n = len(s)
        while i < n or t:
            if i == n or (t and self.compare(t[-1], s[i:])):
                ans += t[-1]
                t.pop()
            else:
                t.append(s[i])
                i += 1
        return ans

    def robotWithString(self, s: str) -> str:
        d = Counter(s)
        q = deque(s)
        sort_keys = sorted(d.keys())
        keys_len = len(sort_keys)
        t = []
        ans = ''
        k = 0
        while q:
            if not q or (t and t[-1] <= sort_keys[k]):
                ans += t[-1]
                t.pop()
            else:
                e = q.popleft()
                t.append(e)
                d[e] -= 1
                if sort_keys[k] == e and d[e] == 0:
                    while k < keys_len and not d[sort_keys[k]]:
                        k += 1
        ans += ''.join(t[::-1])
        return ans

    def suffix_algo(self, s: str) -> str:
        q = deque(s)
        t = []
        ans = ''
        i = 0
        n = len(s)
        suffix = [s[-1]] * n
        for j in range(n - 2, -1, -1):
            suffix[j] = min(s[j], suffix[j + 1])
        while q:
            if t and t[-1] <= suffix[i]:
                ans += t.pop()
            else:
                t.append(q.popleft())
                i += 1
        ans += ''.join(t[::-1])
        return ans

    def test(self, f, n_iter: int = 10000):
        acc = 0
        for _ in range(n_iter):
            s = ''.join(random.choices(letters, k=100))
            slow_ans = self.slow_algo(s=s)
            fast_ans = f(s=s)
            if slow_ans == fast_ans:
                acc += 1
        print(f'Успешно пройдено {acc} из {n_iter} тестов')

    def time_test(self, f, n_iter: int = 100):
        acc = 0
        for _ in range(n_iter):
            s = ''.join(random.choices(letters, k=10**5))
            start = time.perf_counter()
            f(s)
            end = time.perf_counter()
            acc += end - start
        print(f'Общее время работы = {acc:.5f} сек')
        print(f'Среднее время работы = {acc / n_iter:.5f} сек')
