"""
Find Smallest Letter Greater than Target.

Дан массив строчных латинских букв, отсортированный в лексикографическом
порядке. Найти первую букву, которая больше заданного target, или вывести
первую букву массива, если такой нет.

Так как массив отсортирован, то используем бинарный поиск. Если после цикла
индекс right станет равным длине массива, то искомой буквы нет. В ином случае,
right как раз будет указывать на нужную букву.

Лучшее решение: 0 ms, 20.59 Mb
#binary_search #array
"""


class Solution:

    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        length = len(letters)
        left, right = 0, length
        while left < right:
            mid = (left + right) // 2
            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1
        if right == length:
            return letters[0]
        return letters[right]
