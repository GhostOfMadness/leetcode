"""
Validate Binary Search Tree.

Проверить, является ли бинарное дерево деревом поиска.

Лучшее решение: 3 ms, 19.77 Mb
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isValidBST(
        self,
        root: TreeNode,
        low_border: float | int = float('-inf'),
        up_border: float | int = float('inf'),
    ) -> bool:
        ans = low_border < root.val < up_border
        if root.left:
            ans = (
                ans
                and self.isValidBST(
                    root=root.left,
                    low_border=low_border,
                    up_border=root.val,
                )
            )
        if root.right:
            ans = (
                ans
                and self.isValidBST(
                    root=root.right,
                    low_border=root.val,
                    up_border=up_border,
                )
            )
        return ans
