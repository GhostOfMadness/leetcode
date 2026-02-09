"""
Balanced Binary Tree.

Определить, является ли бинарное дерево сбалансированным. Сбалансированное
дерево - дерево, в котором глубина поддеревьев для каждого узла отличается
не более чем на 1.

Создадим переменную класса flag, которая будем отвечать за текущий статус
дерева. Изначально flag = True, так как пустое дерево не противоречит условию.
Рекурсивная функция принимает узел и текущую глубину. Из каждого узла идем
влево и вправо и получаем размеры поддеревьев. Если они отличаются больше чем
на 1, ставим flag на False. Возвращаем значение flag после рекурсии по дереву.

Лучшее решение: 0 ms, 20.83 Mb
#tree #dfs
"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    flag: bool = True

    def isBalanced(self, root: TreeNode) -> bool:

        def rec(node: TreeNode, depth: int = 1) -> int:
            if not node or not self.flag:
                return depth - 1
            left = rec(node.left, depth + 1)
            right = rec(node.right, depth + 1)
            if abs(left - right) > 1:
                self.flag = False
            if left > right:
                return left
            return right

        rec(root)
        return self.flag
