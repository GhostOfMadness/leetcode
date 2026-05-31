"""
Count the Number of Special Characters II

Дана строка word, состоящая из сточных и прописных букв. Буква называется
специальной, если она встречается в строке в обоих регистрах, при этом все
вхождения этой буквы в нижнем регистре идут перед первым вхождением в верхнем
регистре. Найти количество специальных букв в строке.

Заведем массивы lowercase и uppercase размера 26 (по размеру английского
словаря) для работы со строчными и прописными буквами, а также константы
ord_a и ord_A для определения индекса буквы в массиве. Буквы 'a' и 'A' идут
на позиции 0. uppercase[i] = True, если буква chr(ord_A + i) есть в строке,
то есть в uppercase просто храним факт наличия конкретной заглавной буквы.
В lowercase также отмечаем найденные буквы в нижнем регистре, но если для
этой буквы уже есть вхождение загланой, то меняем значение на False, так как
все вхождения строчных букв должны идти строго до заглавной. В качестве ответа
возвращаем количество индексов, где lowercase[i] = True и uppercase[i] = True.

Лучшее решение: 172 ms (91.76%), 20.56 Mb (100%)
#string #array
"""


class Solution:

    def numberOfSpecialChars(self, word: str) -> int:
        lowercase = [False] * 26
        uppercase = [False] * 26
        ord_a = ord('a')
        ord_A = ord('A')
        for letter in word:
            num = ord(letter)
            if num < ord_a:
                uppercase[num - ord_A] = True
            elif uppercase[num - ord_a]:
                lowercase[num - ord_a] = False
            else:
                lowercase[num - ord_a] = True
        return sum(1 for i in range(26) if lowercase[i] and uppercase[i])
