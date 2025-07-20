"""
Top k Frequent Elements.

Найти k элементов, которые встречаются чаще всего в массиве. Гарантируется,
что решение уникально.

С помощью Counter считаем значения и берем k наиболее частых. Так как метод
most_common возвращает список кортежей из пар значение - частота, то за
проход по полученному списку оставляем только исходные значения.

Лучшее решение: 2 ms, 21.35 Mb
"""


from collections import Counter


class Solution:

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [e[0] for e in Counter(nums).most_common(k)]
