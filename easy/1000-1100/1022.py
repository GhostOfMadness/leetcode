"""
Sum of Root to Leaf Binary Numbers.

Дано бинарное дерево, в котором путь от корня к листу представляет собой
двоичную запись целого числа. Найти сумму этих чисел.

Используем поиск в глубину. На каждом шаге рекурсии делаем битовый сдвиг
текущего значения на 1 влево и добавляем значение узла. Если дошли до листа,
то прибавляем полученное число к ответу.

Лучшее решение: 0 ms, 19.63 Mb
#dfs #binary_tree
"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    ans: int = 0

    def sumRootToLeaf(self, root: TreeNode) -> int:

        def rec(node: TreeNode, curr: int) -> None:
            curr = (curr << 1) | node.val
            if not (node.left or node.right):
                self.ans += curr
            else:
                if node.left:
                    rec(node.left, curr)
                if node.right:
                    rec(node.right, curr)

        rec(root, 0)
        return self.ans
