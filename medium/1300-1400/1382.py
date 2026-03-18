"""
Balance a Binary Search Tree.

Необходимо сбалансировать двоичное дерево поиска. То есть глубина поддеревьев
для каждого узла не должна отличаться больше чем на 1.

Сначала используем in-order traversal, чтобы получить отсортированный список
всех значений узлов исходного дерева. В двоичном дереве поиска слева все
значения меньше корня, справа - больше корня. Поэтому порядок левое поддерево
- текущий узел - правое поддерево как раз дает отсортированный массив.

Чтобы дерево было сбалансированным, количество элементов слева и справа от
корня должно отличаться не более чем на 1. То есть корнем будет либо середина
для массива нечетной длины, либо элемент слева/ справа от нее при четной длине.
Корнем левого поддерева будет середина подмассива от начала до корня, корнем
правого - середина от корня до конца. Далее эти части массивов снова будут
делиться на 2 для определения следующих узлов. То есть это рекурсивная функция.
На вход эта рекурсия принимает левую и правую границы участка, правая граница
не включительно. Если левая граница меньше правой, то находим середину участка
nodeIdx и создаем новый узел с val = arr[nodeIdx]. В node.left пойдет ответ
рекурсии на [left: nodeIdx], в node.right - на [nodeIdx + 1, right]. Рекурсия
возвращает узел. При запуске на всем массиве находим корень сбалансированного
дерева.

Лучшее решение: 35 ms, 26.40 Mb
#tree #dfs #divide_and_conquer
"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []

        def inOrder(node: TreeNode) -> None:
            if node:
                inOrder(node.left)
                arr.append(node.val)
                inOrder(node.right)

        inOrder(root)
        left, right = 0, len(arr)

        def rec(left, right):
            if left < right:
                nodeIdx = (left + right) // 2
                node = TreeNode(val=arr[nodeIdx])
                node.left = rec(left, nodeIdx)
                node.right = rec(nodeIdx + 1, right)
                return node

        return rec(left, right)
