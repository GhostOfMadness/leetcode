"""
Subsets.

Дан массив целых чисел nums (числа не повторяются). Вывести все подмассивы,
которые могут быть из него получены. Например, nums = [1, 2],
ans = [[], [1], [2], [1, 2]].

Используем рекурсию. Добавляем очередную цифру к текущему подмассиву,
добавляем его в ответ и запускаем рекурсию от следующего индекса. После
выхода из рекурсии удаляем добавленную цифру. Например, nums = [1, 2, 3],
ans = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]].

Лучшее решение: 0 ms, 17.85 Mb
#array #backtracking
"""


class Solution:

    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = [[]]
        curr = []

        def rec(idx: int = 0):
            for i in range(idx, len(nums)):
                curr.append(nums[i])
                ans.append(curr[:])
                rec(idx=i + 1)
                curr.pop()

        rec()
        return ans
