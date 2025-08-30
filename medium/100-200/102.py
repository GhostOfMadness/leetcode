"""
Binary Tree Level Order Traversal.

Вывести список списков значений узлов бинарного дерева по уровням.

Используем поиск в ширину. В очередь кладем кортеж из пары (узел, уровень,
на котором он находится). Пока очередь не пуста, вынимаем первый элемент.
Если его уровень меньше текущей длины ответа, то в список на соответствующем
индексе добавляем значение узла. В ином случае, добавляем список из значения
узла в конец ответа и увеличиваем длину ответа на 1. Затем добавляем в очередь
левого и правого потомков, если они есть.

Лучшее решение: 0 ms, 18.44 Mb
"""
from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        q = deque([(root, 0)])
        ans = []
        ans_len = 0
        while q:
            curr, level = q.popleft()
            if level < ans_len:
                ans[level].append(curr.val)
            else:
                ans.append([curr.val])
                ans_len += 1
            if curr.left:
                q.append((curr.left, level + 1))
            if curr.right:
                q.append((curr.right, level + 1))
        return ans
