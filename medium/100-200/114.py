"""
Flatten Binary Tree to Linked List.

Необходимо развернуть бинарное дерево в связный список. Список строится на
том же классе, что и узлы дерева, только все значения располагаются справа.

Можно запустить обход в глубину и складывать найденные значения в массив.
Затем пройтись по массиву, создавая новые узлы с текущим значением и добавляя
их справа от текущего корня. У исходного корня перед этим необходимо удалить
левое поддерево.

Если не использовать массив, то общий алгоритм выглядит так:
- распрямить левое поддерево и добавить его справа.
- распрямить правое поддерево и добавить его справа от последнего узла
  с предыдущего шага.

Идем рекурсивно. Если у узла нет детей, то возвращаем его самого, он будет
последним элементом после выпрямления на данном этапе. В ином случае сохраняем
левого и правого потомков, ссылку на левого потомка обнуляем. Если левый
потомок существует, то добавляем его справа от корня и запускаем рекурсию
от него. Если правый потомок существует, то нужно выполнить дополнительную
проверку. Если левый потомок был, то его поддерево уже добавлено справа от
корня, а конец этого поддерева хранится в переменной last. В этом случае
необходимо передвинуть текущий корень на позицию last, иначе - оставить
корень как есть. Справа от корня добавить правого потомка и запустить рекурсию
для него. В общем случае также последний узел после выпрямления.

Лучшее решение: 0 ms, 17.88 Mb
"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def f(self, root: TreeNode) -> TreeNode:
        if not root.left and not root.right:
            return root
        left, right = root.left, root.right
        root.left = None
        last = None
        if left:
            root.right = left
            last = self.f(left)
        if right:
            if last:
                root = last
            root.right = right
            last = self.f(right)
        return last

    def flatten(self, root: TreeNode) -> None:
        """Модификация через рекурсию."""
        if root:
            root = self.f(root)

    def flatten_with_stack(self, root: TreeNode) -> None:
        """Модификация с использованием массива."""
        if root:
            stack = []

            def f(root, stack):
                stack.append(root.val)
                if root.left:
                    f(root.left, stack)
                if root.right:
                    f(root.right, stack)

            f(root, stack)
            root.left = None
            for i in range(1, len(stack)):
                node = TreeNode(val=stack[i])
                root.right = node
                root = node


if __name__ == '__main__':
    res = Solution()
    nodes = [TreeNode(val=i) for i in range(1, 7)]
    root = nodes[0]
    root.left = nodes[1]
    root.right = nodes[4]
    root.left.left = nodes[2]
    root.left.right = nodes[3]
    root.right.right = nodes[5]
    res.flatten(root)
