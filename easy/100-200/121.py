"""
Best Time to Buy and Sell Stock.

Найти такую пару индексов i < j, что разница значений, стоящих на этих индексах
максимальна. Если все разницы отрицательные, то вернуть 0.

Если длина массива равна 1, то ответ 0, так как пар индекс просто нет. В ином
случае, используем жадный подход. В переменную ans заносим максимум из 0 и
разности prices[1] и prices[0]. В переменной curr будем хранить текущий
минимум, сначала выбирая его из пары prices[1], prices[0]. По сути curr
отвечает за минимум на префиксе. Идем по массиву от индекса 2 и до конца.
Наибольшая разница, которая может быть получена со значением prices[i] и
каким-либо элементов перед ним равна prices[i] - curr. При необходимости
обновляем ответ и минимум на префиксе.

Лучшее решение: 37 ms, 28.66 Mb
#array #greedy
"""


class Solution:

    def maxProfit(self, prices: list[int]) -> int:
        length = len(prices)
        if length == 1:
            return 0
        ans = max(0, prices[1] - prices[0])
        curr = min(prices[1], prices[0])
        for i in range(2, length):
            e = prices[i]
            diff = e - curr
            if diff > ans:
                ans = diff
            if e < curr:
                curr = e
        return ans
