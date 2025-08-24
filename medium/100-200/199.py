"""
Binary Tree Right Side View.

Вывести значения узлов бинарного дерева, если смотреть на него справа.

Запускаем рекурсивный поиск в глубину. Так как нужен вид справа, то сначала
идем в правого потомка, потом в левого. В переменной cnt храним номер текущего
уровня. Если cnt больше, чем длина ответа, значит этот узел будет видно,
поэтому заносим его в ответ.

Лучшее решение: 0 ms, 17.66 Mb
"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def rec(self, root: TreeNode, ans: list[int], cnt: int = 1) -> None:
        if cnt > len(ans):
            ans.append(root.val)
        if root.right:
            self.rec(root.right, ans, cnt + 1)
        if root.left:
            self.rec(root.left, ans, cnt + 1)

    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        ans = []
        self.rec(root, ans)
        return ans
