"""
Diameter of Binary Tree.

Найти диаметр бинарного дерева, то есть максимальное количество ребер между
двумя его узлами. Диаметр может не проходить через корень.

Используем поиск в глубину и проверяем каждую вершину как точку перегиба
пути. Для этого получаем максимальное расстояние от левого и правого узлов
до их самых дальниих листьев, суммируем их и прибавляем 2 (2 ребра, которые
идут от текущей вершины влево и вправо). Это наибольшая длина пути с перегибом
в текущем узле. Если эта длина больше текущего максимума, то обновляем его.

Лучшее решение: 3 ms, 22.22 Mb
#dfs #binary_tree
"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ans = [0]

        def rec(node: TreeNode) -> int:
            if not node:
                return -1
            left = rec(node.left) + 1
            right = rec(node.right) + 1
            path = left + right
            if path > ans[0]:
                ans[0] = path
            if left > right:
                return left
            return right

        rec(root)
        return ans[0]
