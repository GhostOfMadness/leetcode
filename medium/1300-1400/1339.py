"""
Maximum Product of Splitted Binary Tree.

Необходимо разделить бинарное дерево на 2 части, удалив одно ребро так, чтобы
максимизировать произведение сумм значений в полученных поддеревьях.

С помощью рекурсии находим суммы значений в каждом поддереве (в том числе и
полном) и сохраняем их в массив. Общую сумма значений сохраняем в переменной
total. Проходимся по массиву и ищем максимальное значение выражения
element * (total - element) для каждого элемента (реализуем с помощью
комбинации функций map и max). Возвращаем ответ по модулю 10 ** 9 + 7.

Лучшее решение: 25 ms, 46.20 Mb
#binary_tree #dfs
"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxProduct(self, root: TreeNode) -> int:
        subtree_sums: list[int] = []

        def tree_sum(root: TreeNode) -> int:
            ans = root.val
            if root.left:
                ans += tree_sum(root.left)
            if root.right:
                ans += tree_sum(root.right)
            subtree_sums.append(ans)
            return ans

        total = tree_sum(root)
        ans = max(map(lambda e: (total - e) * e, subtree_sums))
        return ans % (10 ** 9 + 7)
