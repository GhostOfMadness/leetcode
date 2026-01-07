"""
Maximun Level Sum of a Binary Tree.

Найти уровень бинарного дерева с наименьшей суммой значений узлов. Если
вариантов несколько, то вернуть уровень с наименьшим номером.

Можно решить задачу, используя поиск в ширину или поиск в глубину.

При поиске в ширину также есть варианты. Можно хранить только список узлов
текущего уровня. При проходе по нему считаем сумму значений узлов, обновляем
ответ при необходимости и заносим потомков в новый список, ссылку на который
перекидываем в конце итерации. Также увеличиваем номер уровня на 1. Другим
способом является использование дека из пар (узел, номер уровня). Тогда
извлекаем узлы из начала дека, пока у них совпадают номера уровней, считаем
сумму их значений и обновляем ответ, а потомков кладем в конец дека с уровнем
предка, увеличенным на 1. Первый вариант работает гораздо быстрее, потребление
памяти одинаковое.

Для поиска в глубину создаем массив, где i-й индекс соответствует номеру уровня
при нумерации с 0. В рекурсию передаем узел и его номер уровня. Если этот номер
выходит за пределы массива, то добавляем значение в конец, иначе - увеличиваем
значение на нужном индексе. Для ответа ищем индекс максимума в массиве. Этот
вариант также уступает по времени работы поиску в ширину с массивом для каждого
уровня.

Лучшее время: 6 ms, 23.22 Mb
#binary_tree #bfs #dfs
"""
from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxLevelSum(self, root: TreeNode) -> int:
        """Через список для каждого уровня. 6 ms, 23.22 Mb"""
        ans_sum = float('-inf')
        ans_lvl = 0
        curr = [root]
        curr_lvl = 1
        while curr:
            next_lvl = []
            curr_sum = 0
            for node in curr:
                if node.left:
                    next_lvl.append(node.left)
                if node.right:
                    next_lvl.append(node.right)
                curr_sum += node.val
            if curr_sum > ans_sum:
                ans_sum = curr_sum
                ans_lvl = curr_lvl
            curr_lvl += 1
            curr = next_lvl
        return ans_lvl

    def maxLevelSum2(self, root: TreeNode) -> int:
        """Через дек. 29 ms, 23.06 Mb"""
        ans_sum = float('-inf')
        ans_lvl = 0
        curr = deque([(root, 1)])
        curr_lvl = 1
        while curr:
            curr_sum = 0
            while curr and curr[0][1] == curr_lvl:
                node, node_lvl = curr.popleft()
                curr_sum += node.val
                if node.left:
                    curr.append((node.left, node_lvl + 1))
                if node.right:
                    curr.append((node.right, node_lvl + 1))
            if curr_sum > ans_sum:
                ans_sum = curr_sum
                ans_lvl = curr_lvl
            curr_lvl += 1
        return ans_lvl

    def maxLevelSum3(self, root: TreeNode) -> int:
        """Через поиск в глубину. 23 ms, 22.80 Mb список"""
        l: list[int] = []

        def rec(node: TreeNode, lvl: int = 1) -> None:
            if lvl > len(l):
                l.append(node.val)
            else:
                l[lvl - 1] += node.val
            if node.right:
                rec(node.right, lvl + 1)
            if node.left:
                rec(node.left, lvl + 1)

        rec(root)
        return l.index(max(l)) + 1
