"""
Minimum Cost to Convert String I.

Даны строки source и target одинаковой длины, состоящие из строчных латинских
букв. Также даны три массива original, changed, cost равного размера, которые
определяют возможность перевода буквы original[i] в changed[i] за cost[i].
Найти минимальную стоимость приведения строки source к target. Количество
операций изменения символа не ограничено. Вернуть -1, если перевод невозможен.

Массивы original и changed задают прямой перевод одной буквы в другую, но так
как количество операций неограничено, то можно двигаться по цепочке переводов,
чтобы достичь нужной буквы за меньшую стоимость или впринципе достичь ее, если
прямого перехода нет. Перевод одной буквы в другую похож на ребро с весом в
ориентированном графе. Если собрать из массивов граф, то задача сводится
к поиску кратчайших путей от каждой из вершин графа до всех остальных. Тогда
мы получим словарь для перевода символов и за линейное время сможем перевести
строку. Кратчайшие пути от каждой вершины можно найти алгоритмом Дейкстры,
так как стоимость неотрицательна.

Сначала представляем массивы original, changed, cost в виде словаря смежности
(так как узлами являются строки, а не числа), где каждой букве алфавита
соответствует список кортежей "(буква перевода, стоимость перевода)". Из
каждой буквы запускаем алгоритм Дейкстры, чтобы в итоге получить словарь, где
букве соответствует словарь "буква перевода": "оптимальная стоимость". Алгоритм
Дейкстры реализован на бинарной мин-куче для выбора минимума, но без удаления
старых значений, пока они не окажутся на вершине. Это увеличивает расход
памяти, но снижает время на выбор следующей вершины. После получения словаря
проходимся по строкам source и target и суммируем стоимость перевода символов.
Если в ответе получили бесконечность, то какой-то из символов нельзя перевести,
значит возвращаем -1, иначе - выдаем найденное число.

Лучшее решение: 423 ms, 21.62 Mb
#graph_theory #heap #shortest_path
"""
import heapq
import math

from string import ascii_lowercase as letters


class Solution:

    def dijkstra(
        self,
        g: dict[str, list[tuple[str, int]]],
    ) -> dict[str, dict[str, int | float]]:
        res = {letter: {lt: float('inf') for lt in g} for letter in g}
        for letter in g:
            res[letter][letter] = 0
        for start in g:
            dist = res[start]
            heap = [(float('inf'), k) for k in g]
            heap.append((0, start))
            heapq.heapify(heap)
            while True:
                c, letter = heapq.heappop(heap)
                while heap and dist[letter] != c:
                    c, letter = heapq.heappop(heap)
                if math.isinf(c):
                    break
                for node, cost in g[letter]:
                    val = c + cost
                    if val < dist[node]:
                        dist[node] = val
                        heapq.heappush(heap, (val, node))
        return res

    def minimumCost(
        self,
        source: str,
        target: str,
        original: list[str],
        changed: list[str],
        cost: list[int],
    ) -> int:
        g = {lt: [] for lt in letters}
        for i in range(len(original)):
            letter = original[i]
            g[letter].append((changed[i], cost[i]))
        res = self.dijkstra(g)
        ans = sum(res[l1][l2] for l1, l2 in zip(source, target))
        if math.isinf(ans):
            return -1
        return ans
