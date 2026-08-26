"""
Create Binary Tree From Descriptions.

Дан массив descriptions, задающий описание бинарного целочисленного дерева,
в котором значения не повторяются. descriptions[i] = [parent, child, isLeft],
т.е. child[i] является левым потомком parent[i], если isLeft[i] == 1, в ином
случае - правым потомком. По полученному массиву необходимо построить бинарное
дерево и вернуть его корень.

Заведем словарь val_node, в котором для каждого числа будем хранить его узел
в дереве (допустимо, так как числа не повторяются), и множество root_options,
чтобы затем определить корень. Идем циклом по всем элементам в descriptions.
Если родительского узла нет в val_node, то создаем его, и добавляем значение
родителя в root_options как потенциальное значение корня. Если в словаре нет
узла-потомка, то создаем его. Если узел-потомок был потенциальным корнем до
текущего шага, то удаляем его значение из root_options. Цепляем потомка слева
или справа от родителя в зависимости от значения isleft. После цикла в
root_options останется только значение корня, так как массив descriptions по
условию задает корректное описание бинарного дерева. Возвращаем узел,
соответствующий этому значению.

Лучшее решение: 105 ms (99.80%), 26.79 Mb (97.76%)
#array #hash_table #binary_tree
"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode:
        val_node = {}
        root_options = set()
        for e in descriptions:
            p, c, isleft = e
            if p not in val_node:
                val_node[p] = TreeNode(p)
                root_options.add(p)
            if c not in val_node:
                val_node[c] = TreeNode(c)
            if c in root_options:
                root_options.remove(c)
            if isleft:
                val_node[p].left = val_node[c]
            else:
                val_node[p].right = val_node[c]
        return val_node[root_options.pop()]
