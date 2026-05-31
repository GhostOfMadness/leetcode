"""
Find the Length of the Longest Common Prefix.

Даны два массива целых положительных чисел arr1 и arr2. Найти наибольшую длину
префикса среди всех пар чисел x и y, где x лежит в arr1, y - в arr2.

Используем префиксное дерево. Все числа из массива arr1 переводим в строки
и по цифре заносим в дерево trie, построенное на словарях. Числа в arr2 также
переводим в строки. Для каждого числа идем от корня дерева и считаем кол-во
шагов (то есть глубину спуска). Выбираем максимальный счетчик.

Лучшее решение: 203 ms (80.25%), 32.32 Mb (37.34%)
#trie #array #hash_table
"""


class Solution:

    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        trie = {'': {}}
        for num in arr1:
            snum = str(num)
            root = trie['']
            for digit in snum:
                if digit not in root:
                    root[digit] = {}
                root = root[digit]
        ans = 0
        for num in arr2:
            snum = str(num)
            root = trie['']
            cnt = 0
            for digit in snum:
                if digit not in root:
                    break
                cnt += 1
                root = root[digit]
            if cnt > ans:
                ans = cnt
        return ans
