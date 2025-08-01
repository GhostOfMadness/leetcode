"""
Palindrom Number.

Необходимо проверить, является ли число палиндромом.

Лучшее решение: 0 ms, 17.80 Mb
"""


class Solution:

    def isPalindrome_to_str(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]

    def isPalindrome_to_int(self, x: int) -> bool:
        if x < 0:
            return False
        old_x = x
        reverse_x = 0
        while old_x // 10:
            reverse_x = reverse_x * 10 + old_x % 10
            old_x //= 10
        reverse_x = reverse_x * 10 + old_x % 10
        return x == reverse_x
