"""
Lexicographically Minimum String After Removing Stars.

Необходимо найти лексикографическую наименьшую строку, которая получается
после удаление всех символов '*' и наименьшего элемента слева от нее (если
таких несколько, то можно удалить любой).

Лучшее решение: 279 ms, 22.70 Mb
"""


import heapq

from string import ascii_lowercase as letters


class Solution:

    def clearStars(self, s: str) -> str:
        d = {letter: [] for letter in letters}
        q = []
        heapq.heapify(q)
        ans = list(s)
        for i in range(len(s)):
            letter = s[i]
            if letter == '*':
                ans[i] = ''
                idx = d[q[0]].pop()
                ans[idx] = ''
                if not d[q[0]]:
                    heapq.heappop(q)
            else:
                if not d[letter]:
                    heapq.heappush(q, letter)
                d[letter].append(i)
        return ''.join(ans)
