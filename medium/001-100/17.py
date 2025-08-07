"""
Letter Combinations of a Phone Number.

Необходимо найти все варинты текстового сообщения по данному набору цифр.

Сначала создадим словарь d, в котором сохраним для каждой цифры
соответствующие буквы. Для каждой буквы текущей цифры будем запускать рекурсию
и накапливать строку. Когда дошли до конца (прошли все цифры), добавляем
полученную строку в ответ.

Лучшее решение: 0 ms, 17.63 Mb
"""


class Solution:

    d = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def rec(
        self,
        digits: str,
        pos: int,
        ans: list[str],
        curr: str,
        n: int,
    ) -> None:
        if pos == n:
            ans.append(curr)
        else:
            for letter in self.d[digits[pos]]:
                self.rec(digits, pos + 1, ans, curr + letter, n)

    def letterCombinations(self, digits: str) -> list[str]:
        ans = []
        n = len(digits)
        if n:
            self.rec(digits=digits, pos=0, ans=ans, curr='', n=n)
        return ans


if __name__ == '__main__':
    res = Solution()
    digits = '23'
    print(res.letterCombinations(digits))
