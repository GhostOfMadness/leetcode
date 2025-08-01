"""
Find the Original Typed String I.

При вводе строки пользователь мог не больше 1 раза зажать какую-то клавишу
и напечатать букву несколько раз. Найти количество возможных строк, которые
хотел ввести пользователь.

Лучшее решение: 41 ms, 17.82 Mb
"""


class Solution:

    def possibleStringCount(self, word: str) -> int:
        return (
            sum(1 for i in range(1, len(word)) if word[i] == word[i - 1])
            + 1
        )
