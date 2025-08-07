"""
Fruits Into Baskets III.

Массив fruits содержит количество фруктов каждого типа, массив baskets -
вместимость корзин. Массивы имеют одинаковый размер. Каждый новый тип фрукта
нужно положить в первую подходящую по вместимости корзину слева. Найти кол-во
типов фруктов, которые не будут распределены по корзинам.

Воспользуемся деревом отрезков, в котором будем хранить максимумы. Сначала
определяем размер нижнего уровня этого дерева, для этого увеличиваем исходный
размер массива baskets до ближайшей степени двойки (__get_tree_len). Найденное
значение сохраним в n. Исходные элементы заносим с позиции n - 1. Далее идем
справа налево от позиции n - 2. Каждое значение будет равно максимуму из двух
уже посчитанных потомков на индексах 2 * i + 1 и 2 * i + 2.

Проходимся по каждому элементу fruits. Если элемент не больше корня дерева,
то для него есть подходящая корзина. Идем в глубину, на каждом шаге отдавая
предпочтение левому потомку, если его значение не меньше элемента fruits.
Когда нашли нужную корзину, то ставим ее значение на 0, а также обновляем
значения всех предков. Уменьшаем счетчик fruits_left, который изначально
равен общему числу элементов fruits, на 1. В качестве ответа возвращаем
fruits_left.

Лучшее решение: 1532 ms, 39.11 Mb
"""


class Solution:

    def __get_tree_len(self, length: int):
        curr = 1
        while length > curr:
            curr *= 2
        return curr

    def __get_segment_tree(self, baskets: list[int]) -> tuple[list[int], int]:
        n = self.__get_tree_len(len(baskets))
        tree = [0] * (2 * n - 1)
        for i in range(len(baskets)):
            tree[i + n - 1] = baskets[i]
        for i in range(n - 2, -1, -1):
            tree[i] = max(tree[2 * i + 1], tree[2 * i + 2])
        return tree, n

    def numOfUnplacedFruits(
        self,
        fruits: list[int],
        baskets: list[int],
    ) -> int:
        tree, n = self.__get_segment_tree(baskets)
        fruit_left = len(fruits)
        for fruit in fruits:
            if fruit <= tree[0]:
                i = 0
                while i < n - 1:
                    left = 2 * i + 1
                    right = 2 * i + 2
                    if fruit <= tree[left]:
                        i = left
                    else:
                        i = right
                tree[i] = 0
                anc = (i - 1) // 2
                while anc >= 0:
                    tree[anc] = max(tree[2 * anc + 1], tree[2 * anc + 2])
                    anc = (anc - 1) // 2
                fruit_left -= 1
        return fruit_left
