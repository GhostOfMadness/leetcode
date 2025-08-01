"""
Valid Word.

Слово считается правильным, если состоит только из английских букв в любом
регистре, имеет длину не меньше 3, содержит минимум одну букву из набора
'aeiouAEIOU' и минимум 1 любую другую букву. Проверить слово.

Лучшее решение: 0 ms, 17.81 Mb
"""


import re

from string import ascii_lowercase as letters


class Solution:

    def isValid(self, word: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        consonants = set(letters) - vowels
        word_set = set(word.lower())
        return bool(
            re.fullmatch(r'[0-9a-zA-Z]{3,}', word)
            and word_set & vowels
            and word_set & consonants
        )


if __name__ == '__main__':
    res = Solution()
    word = '234Adas'
    print(res.isValid(word))
