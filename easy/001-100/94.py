"""
Binary Tree Inorder Traversal.

Вывести порядок прохождения узлов при центрированном обходе дереве (LNR).

Используем поиск в глубину. Сначала идем в левое поддерево, затем заносим
значение текущего узла, потом идем в правое поддерево.

Лучшее решение: 0 ms, 19.32 Mb
#binary_tree #dfs
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        res = []

        def dfs(node: TreeNode) -> None:
            if node:
                dfs(node.left)
                res.append(node.val)
                dfs(node.right)

        dfs(root)
        return res
