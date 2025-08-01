"""
Maximum Erasure Value.

Найти последовательный подмассив с наибольшей суммой элементов, каждый из
которых уникален для этого подмассива.

В словаре val_idx будем хранить пары значение - индекс для текущего подмассива.
Если новое число уже встречалось в подмассиве, то обновляем ответ и удаляем
из словаря все значения, которые встречались до него, попутно сокращая
текущее значение суммы. Кладем новое число в словарь и обновляем сумму
(это же происходит, если новое число в словаре не лежит).

Лучшее решение: 165 ms, 29.05 Mb
"""


class Solution:

    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        val_idx = {}
        ans = 0
        curr = 0
        left = 0
        for i in range(len(nums)):
            num = nums[i]
            if num in val_idx:
                ans = max(ans, curr)
                while num in val_idx:
                    curr -= nums[left]
                    val_idx.pop(nums[left])
                    left += 1
            val_idx[num] = i
            curr += num
        return max(ans, curr)
