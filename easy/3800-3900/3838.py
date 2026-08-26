"""
Weighted Word Mapping.

Дан массив строк words и массив weights, weights[i] - вес i-й буквы в словаре
при нумерации с нуля. Весом слова считается сумма весов его букв. Для каждого
слова необходимо вычислить его вес, взять остаток от деления этого веса на 26
и записать в ответ букву развернутого алфавита, т.е. 0 = 'z', 1 = 'y' и т.д.

Используем симуляцию процесса и объединяем буквы в ответе.

Лучшее решение: 5 ms (88.22%), 19.39 Mb (33.64%)
#array #string #simulation
"""


class Solution:

    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        ans = []
        ord_a = ord('a')
        for word in words:
            curr = 0
            for letter in word:
                curr += weights[ord(letter) - ord_a]
            curr %= 26
            ans.append(chr(25 - curr + ord_a))
        return ''.join(ans)
