"""
Roman to Integer.

Перевести число, записанное римскими цифрами, в привычную запись.

Лучшее решение: 6 ms, 17.90 Mb
"""


class Solution:

    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        ans = 0
        prev = 0
        for i in range(len(s) - 1, -1, -1):
            curr = d[s[i]]
            if curr < prev:
                ans -= curr
            else:
                ans += curr
            prev = curr
        return ans
