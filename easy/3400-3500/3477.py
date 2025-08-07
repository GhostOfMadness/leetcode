"""
Fruits Into Baskets II.

Массив fruits содержит количество фруктов каждого типа, массив baskets -
вместимость корзин. Массивы имеют одинаковый размер. Каждый новый тип фрукта
нужно положить в первую подходящую по вместимости корзину слева. Найти кол-во
типов фруктов, которые не будут распределены по корзинам.

Запускаем симуляцию этого выбора (O(n ** 2)), для выбранных корзин
устанавливаем значение на 0 и уменьшаем счетчик оставшихся корзин left.
Возвращаем left.

Лучшее решение: 19 ms, 17.73 Mb
"""


class Solution:

    def numOfUnplacedFruits(
        self,
        fruits: list[int],
        baskets: list[int],
    ) -> int:
        n = len(fruits)
        left = n
        for i in range(n):
            for j in range(n):
                if baskets[j] >= fruits[i]:
                    baskets[j] = 0
                    left -= 1
                    break
        return left
