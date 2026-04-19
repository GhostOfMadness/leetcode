"""
Shortest Distance to Target String in a Circular Array.

Дан циклический массив слов words, искомое слово target и начальный индекс
startIndex. От начального индекса можно двигаться как влево, так и вправо.
Найти кратчайшее расстояние до искомого слова от начального индекса или
вывести -1, если такого слова нет в массиве.

Перебираем все слова массива. Если текущее слово равно искомому, то считаем
расстояние от начального индекса до текущего. По часовой стрелке это будет
(idx - startIndex) % n, idx - текущий индекс, n - размер массива words. Против
часовой стрелки - (startIndex - idx) % n. Выбираем минимальное и обновляем
ответ.

Лучшее решение: 0 ms, 19.52 Mb
#string
"""
import math


class Solution:

    def closestTarget(
        self,
        words: list[str],
        target: str,
        startIndex: int,
    ) -> int:
        n = len(words)
        ans = float('inf')
        for idx in range(n):
            if words[idx] == target:
                ans = min(ans, (idx - startIndex) % n, (startIndex - idx) % n)
        if math.isinf(ans):
            return -1
        return ans
