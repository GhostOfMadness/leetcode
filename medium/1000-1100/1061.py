"""
Lexicographically Smallest Equivalent String.

Исходные строки s1 и s2 считаются равными, то есть s1[i] == s2[i].
Это равенство обладает свойствами симметричности и транзитивности.
Найти лексикографически наименьшую строку, в которую можно преобразовать
baseStr, использую равенство строк s1 и s2.

Лучшее решение: 0 ms, 17.70 MB
"""


from string import ascii_lowercase as letters


class Solution:

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        d = {letter: letter for letter in letters}
        for i in range(len(s1)):
            root1 = d[s1[i]]
            while root1 != d[root1]:
                root1 = d[root1]
            root2 = d[s2[i]]
            while root2 != d[root2]:
                root2 = d[root2]
            if root1 < root2:
                d[root2] = root1
            else:
                d[root1] = root2
        ans = ''
        for letter in baseStr:
            while letter != d[letter]:
                letter = d[letter]
            ans += letter
        return ans
