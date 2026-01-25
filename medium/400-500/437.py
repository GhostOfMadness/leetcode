"""
Path Sum III.

Найти количество вертикальных путей, т.е. от предка к потомку без перегибов,
сумма значений узлов на которых равна заданному значению. Путь не обязан
начинаться в корне или заканчиваться в листе.

Используем поиск в глубину в сочетании с префиксными суммами. Снаружи рекурсии
создаем словарь cnt, в котором будем хранить "отрицательный префикс: частота
этого префикса". Запись отрицательных префиксов позволит хранить все варианты
путей до узла, без необходимости их пересчета на каждом новом узле. В рекурсию
передается узел, а также значение префикса, равное сумме значений узлов от
корня до предка. Увеличиваем значение префикса на текущее значение и ищем
величину targetSum - prefix в словаре. В cnt хранятся отрицательные значения
префиксов, поэтому при добавлении положительного накопленного значения к
каждому из них как раз получаем варианты путей от предка на каждом уровне до
теущего узла. Ищем targetSum - prefix, чтобы не проверять все линейно. Если
такое значение есть, то увеличиваем ответ на количество таких путей. Затем
заносим префикс со знаком минус в cnt. Если это новый ключ, то его значением
будет 1, если нет - то увеличиваем имеющееся значение на 1. Запускаем рекурсию
для левого и правого потомков. Удаляем одно вхождение пути -prefix из словаря,
после обхода поддеревьев, так как при проверке других путей этот вариант не
должен учитываться. Если значение ключа стало равным 0, то удаляем этот ключ.

Лучшее решение: 1 ms, 20.03 Mb
#binary_tree #prefix_sum #dfs
"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    ans: int = 0

    def pathSum(self, root: TreeNode, targetSum: int) -> int:

        cnt: dict[int, int] = {0: 1}

        def rec(node: TreeNode, prefix: int = 0):
            if node:
                prefix += node.val
                neg_prefix = -prefix
                s = targetSum - prefix
                if s in cnt:
                    self.ans += cnt[s]
                cnt[neg_prefix] = cnt.get(neg_prefix, 0) + 1
                rec(node.left, prefix)
                rec(node.right, prefix)
                cnt[neg_prefix] -= 1
                if not cnt[neg_prefix]:
                    cnt.pop(neg_prefix)

        rec(root)
        return self.ans


res = Solution()
l1 = TreeNode(val=3)
l2 = TreeNode(val=-2)
l3 = TreeNode(val=1)
l4 = TreeNode(val=11)
n1 = TreeNode(val=3, left=l1, right=l2)
n2 = TreeNode(val=2, right=l3)
n3 = TreeNode(val=5, left=n1, right=n2)
n4 = TreeNode(val=-3, right=l4)
root = TreeNode(val=10, left=n3, right=n4)
target = 8
# l1 = TreeNode(val=7)
# l2 = TreeNode(val=2)
# l3 = TreeNode(val=13)
# l4 = TreeNode(val=5)
# l5 = TreeNode(val=1)
# n1 = TreeNode(val=11, left=l1, right=l2)
# n2 = TreeNode(val=4, left=n1)
# n3 = TreeNode(val=4, left=l4, right=l5)
# n4 = TreeNode(val=8, left=l3, right=n3)
# root = TreeNode(val=5, left=n2, right=n4)
# target = 22
print(res.pathSum3(root, target))
