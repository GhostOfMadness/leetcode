"""
Longest Substring Without Repeating Characters.

Найти длину наибольшой последовательной подстроки, в которой символы не
повторяются.

В словаре val_idx будем хранить пары значение - индекс для текущей подстроки.
Также заведем 2 указателя left и right на границы подстроки. Если новый символ
уже встречался в подстроке, то обновляем ответ и удаляем из словаря все
значения, которые встречались до него, сдвигая левый указатель. Кладем новый
символ в словарь и сдвигаем правый указатель на 1 (это же происходит, если
новый символ в словаре не лежит).

Лучшее решение: 11 ms, 17.86 Mb
"""


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        val_idx = {}
        ans = 0
        left = 0
        right = 0
        for e in s:
            if e in val_idx:
                ans = max(ans, right - left)
                while e in val_idx:
                    val_idx.pop(s[left])
                    left += 1
            val_idx[e] = right
            right += 1
        return max(ans, right - left)
