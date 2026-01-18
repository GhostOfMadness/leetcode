"""
Maximum Depth of a Binary Tree.

Найти глубину бинарного дерева.

Используем поиск в глубину. Каждый вызов рекурсии возвращает глубину поддерева,
корнем которого является текущий узел.

Лучшее решение: 0 ms, 20.27 Mb
#binary_tree #dfs
"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepth(self, root: TreeNode) -> int:

        def dfs(node: TreeNode, depth: int = 1):
            if not node:
                return depth - 1
            return max(
                dfs(node.left, depth + 1),
                dfs(node.right, depth + 1),
            )

        return dfs(root)
