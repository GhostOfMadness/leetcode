"""
Minimum Distance to the Target Element.

Дан массив целых положительных чисел nums, индекс start и число target,
которое точно есть в массиве. Найти минимальное расстояние от позиции start
до любой позиции target в массиве.

Задаем ответ как float('inf'). Сначала идем влево от start. Если там есть
число target, то ans = start - i, так как при таком движении start >= i.
Выходим из цикла при первом найденном совпадении, так как далее расстоние
будет только увеличиваться. Затем идем вправо от start и повторяем поиск. В
случае нахождения числа в ответ берем минимум из текущего значения ответа
и i - start. Также выходим из цикла при первом совпадении.

Лучшее решение: 0 ms, 19.29 Mb
#array
"""
import random

from test_class import Test


class Solution(Test):

    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        ans = float('inf')
        for i in range(start, -1, -1):
            if nums[i] == target:
                ans = start - i
                break
        for i in range(start + 1, len(nums)):
            if nums[i] == target:
                ans = min(ans, i - start)
                break
        return ans

    def data_genr(self, **kwargs):
        size = 10 ** 6
        nums = random.choices(range(1, 10 ** 4 + 1), k=size)
        target_idx = random.randint(0, size - 1)
        target = nums[target_idx]
        start = random.randint(0, size - 1)
        return dict(nums=nums, target=target, start=start)


res = Solution()
res.time_test([res.getMinDistance, res.getMinDistance2], n_iter=10 ** 2)
