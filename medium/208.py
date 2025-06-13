"""
Implement Trie (Prefix Tree).

Реализация префиксного дерева. Каждый узел - массив из 2-х элементов:
1. Булевое значение, которое показывает, является ли данный узел концом слова.
2. Словарь дочерних узлов, ключ - соответствующая буква.

Лучшее решение: 30 ms, 32.65 Mb
"""


class Trie:

    def __init__(self) -> None:
        self.root = [False, {}]

    def __depthSearch(self, word: str, insert: bool = False) -> None | list:
        curr = self.root
        for letter in word:
            if letter not in curr[1]:
                if not insert:
                    return None
                curr[1][letter] = [False, {}]
            curr = curr[1][letter]
        return curr

    def insert(self, word: str) -> None:
        curr = self.__depthSearch(word=word, insert=True)
        curr[0] = True

    def search(self, word: str) -> bool:
        curr = self.__depthSearch(word=word)
        return bool(curr and curr[0])

    def startsWith(self, prefix: str) -> bool:
        curr = self.__depthSearch(word=prefix)
        return bool(curr)


if __name__ == '__main__':
    trie = Trie()
    trie.insert('apple')
    print(trie.search('apple'))
    print(trie.search('app'))
    print(trie.startsWith('app'))
    trie.insert('app')
    print(trie.search('app'))
