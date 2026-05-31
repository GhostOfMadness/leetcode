"""
 Count the Number of Special Characters I.

Дана строка word, состоящая из прописных и строчных латинских букв. Буква
считается специальной, если она присутствует в слове в обоих регистрах. Найти
количество специальных букв.

Проходимся по строке и создаем множества строчных и прописных букв. Буквы в
верхнем регистре переводим в нижний перед добавлением. В качестве ответа
возвращаем длину пересечения этих множеств.

Лучшее решение: 0 ms (100%), 19.31 Mb (25.31%)
#string #hash_table
"""


class Solution:

    def numberOfSpecialChars(self, word: str) -> int:
        lowercase = set()
        uppercase = set()
        for letter in word:
            if letter.islower():
                lowercase.add(letter)
            else:
                uppercase.add(letter.lower())
        return len(lowercase & uppercase)
